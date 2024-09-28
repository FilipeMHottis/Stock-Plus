from ..core.database import BaseModel, db
from ..core.types import ProductInfo, SaleInfo

from .user_model import User
from .payment_method_model import PaymentMethod
from .product_model import Product

from peewee import (
    DateTimeField,
    DecimalField,
    ForeignKeyField,
    DoesNotExist,
)
from datetime import datetime, timedelta
from typing import List, Optional


class Sale(BaseModel):
    user_id = ForeignKeyField(User, backref="sales", null=False)
    sale_date = DateTimeField(default=datetime.now)
    payment_method_id = ForeignKeyField(
        PaymentMethod,
        backref="sales",
        null=False,
    )
    discount = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
    )

    class Meta:
        database = db
        table_name = "sales"

    def get_complete_sale(self) -> SaleInfo:
        """
        Returns a detailed sale object with information about the user,
        payment method, and products.
        """

        from .sale_product_model import SaleProduct  # Mova o import aqui

        # Fetch related products with quantities in the sale

        sale_products = (
            SaleProduct.select(SaleProduct, Product)
            .join(Product)
            .where(SaleProduct.sale_id == self.id)
        )

        products_info: List[ProductInfo] = []
        for sale_product in sale_products:
            products_info.append(
                {
                    "product_id": sale_product.product.id,
                    "product_name": sale_product.product.name,
                    "quantity": sale_product.quantity,
                    "price": float(
                        sale_product.product.price
                    ),  # Converting Decimal to float
                    "total_price": float(
                        sale_product.quantity * sale_product.product.price
                    ),  # Converting Decimal to float
                }
            )

        # Assemble the return object with correct typing
        return SaleInfo(
            sale_id=self.id,
            user={
                "user_id": self.user_id.id,
                "name": self.user_id.name,
                "role": self.user_id.role,
            },
            sale_date=self.sale_date.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),  # Formatting the date
            payment_method={
                "payment_method_id": self.payment_method_id.id,
                "method": self.payment_method_id.method,
            },
            discount=float(self.discount),  # Converting Decimal to float
            products=products_info,
            total_sale_price=sum(item["total_price"] for item in products_info)
            - float(self.discount),
        )

    @classmethod
    def get_all(cls, sale_date: Optional[datetime] = None) -> List[SaleInfo]:
        """
        Returns all sales. If a date is provided,
        returns only the sales of that day.
        By default, the current day is used.
        """
        if sale_date is None:
            # If no date is provided, return all sales
            sales = cls.select()
        else:
            # Define the start and end of the provided day
            start_date = sale_date.replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0,
            )
            end_date = start_date + timedelta(days=1)

            # Fetch all sales within the date range
            sales = cls.select().where(
                cls.sale_date.between(
                    start_date,
                    end_date,
                )
            )

        # Convert each sale to SaleInfo
        return [sale.get_complete_sale() for sale in sales]

    @classmethod
    def get_by_id(cls, sale_id: int) -> Optional[SaleInfo]:
        """
        Returns a sale based on its ID.
        """
        try:
            sale = cls.get(cls.id == sale_id)
            return sale.get_complete_sale()
        except DoesNotExist:
            return None  # Return None if the sale does not exist

    @classmethod
    def get_by_user_id(
        cls,
        user_id: int,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> List[SaleInfo]:
        """
        Returns the sales of a user with
        the possibility to filter by a date range.
        By default, the range is the current day.
        """
        if start_date is None:
            start_date = datetime.now().replace(
                hour=0, minute=0, second=0, microsecond=0
            )  # Start of the day
        if end_date is None:
            end_date = start_date + timedelta(days=1)  # End of the day

        # Fetch all sales of the user within the date range
        sales = cls.select().where(
            (cls.user_id == user_id)
            & (
                cls.sale_date.between(
                    start_date,
                    end_date,
                )
            )
        )

        # Convert each sale to SaleInfo
        return [sale.get_complete_sale() for sale in sales]
