from ..core.database import BaseModel, db
from .product_model import Product
from .sale_model import Sale  # Importação de Sale deve vir aqui

from peewee import (
    ForeignKeyField,
    IntegerField,
)


class SaleProduct(BaseModel):
    sale_id = ForeignKeyField(Sale, backref="products", null=False)
    product_id = ForeignKeyField(Product, backref="sales", null=False)
    quantity = IntegerField(null=False)

    class Meta:
        database = db
        table_name = "sale_products"
