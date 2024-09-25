from ..core.database import BaseModel
from .sale_model import Sale
from .product_model import Product
from peewee import IntegerField, ForeignKeyField


class SaleProduct(BaseModel):
    sale_id = ForeignKeyField(Sale, backref="sale_products", null=False)
    product_id = ForeignKeyField(Product, backref="product_sales", null=False)
    quantity = IntegerField(null=False)
