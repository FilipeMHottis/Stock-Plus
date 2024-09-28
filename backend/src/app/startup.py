from fastapi import FastAPI
from ..model.user_model import User
from ..model.product_model import Product
from ..model.payment_method_model import PaymentMethod
from ..model.sale_model import Sale
from ..model.sale_product_model import SaleProduct

from ..core.security import Security
from ..core.database import db
from ..core.config import Config


async def create_db(app: FastAPI):
    if db.is_closed():
        db.connect()

    try:
        db.create_tables(
            [User, Sale, Product, SaleProduct, PaymentMethod],
            safe=True,
        )

        await create_admin_user()
    finally:
        if not db.is_closed():
            db.close()

    yield


async def create_admin_user():
    admim = {
        "name": Config.admin_user.get("name"),
        "username": Config.admin_user.get("username"),
        "email": Config.admin_user.get("email"),
        "password": Config.admin_user.get("password"),
    }

    with db.connection_context():
        if not User.select().where(User.username == "admin").exists():
            hashed_password = Security.hash_password(admim.get("password"))
            User.create(
                name=admim.get("name"),
                username=admim.get("username"),
                email=admim.get("email"),
                password_hash=hashed_password,
                role="admin",
            )
