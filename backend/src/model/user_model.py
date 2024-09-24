from ..core.database import BaseModel
from datetime import datetime
from peewee import CharField, BooleanField, DateTimeField


class User_Model(BaseModel):
    # Field Name: name
    name = CharField(max_length=255, null=False)  # Required (cannot be null)

    # Field Name: username
    username = CharField(
        max_length=50,
        unique=True,  # Must be unique
        null=False,  # Required (cannot be null)
    )

    # Field Name: email
    email = CharField(
        max_length=100,
        unique=True,  # Must be unique
        null=False,  # Required (cannot be null)
    )

    # Field Name: password_hash
    password_hash = CharField(null=False)  # Required (cannot be null)

    # Field Name: role
    role = CharField(
        max_length=20,
        default="cashier",  # Default value: "cashier"
    )

    # Field Name: is_active
    is_active = BooleanField(default=True)  # Default value: True

    # Field Name: created_at
    created_at = DateTimeField(
        default=datetime.now  # Default value: Current date and time
    )
