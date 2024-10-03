from ..core.database import BaseModel, db
from datetime import datetime
from peewee import CharField, BooleanField, DateTimeField


class User(BaseModel):
    name = CharField(max_length=255, null=False)
    username = CharField(max_length=50, unique=True, null=False)
    email = CharField(max_length=100, unique=True, null=False)
    password_hash = CharField(null=False)
    role = CharField(max_length=20, default="cashier")
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = "users"
