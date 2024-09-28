from ..core.database import BaseModel, db
from peewee import CharField


class PaymentMethod(BaseModel):
    method = CharField(max_length=50, unique=True, null=False)
    description = CharField(max_length=255, null=True)

    class Meta:
        database = db
        table_name = "payment_methods"
