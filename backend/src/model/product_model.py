from ..core.database import BaseModel
from datetime import datetime
from peewee import CharField, IntegerField, DecimalField, DateTimeField


class Product(BaseModel):
    name = CharField(max_length=255, null=False)
    description = CharField(max_length=255, null=False)
    price = DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = IntegerField(default=0)
    barcode = CharField(max_length=50, unique=True, null=True)
    custom_code = CharField(max_length=50, unique=True, null=True)
    image_url = CharField(max_length=255, null=True)
    created_at = DateTimeField(default=datetime.now)
