import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1"]
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")

    DB = {
        "user": os.getenv("DB_USER", "user"),
        "password": os.getenv("DB_PASSWORD", "password"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", 5432)),
        "database": os.getenv("DB_NAME", "sqlite"),
    }

    admin_user = {
        "name": os.getenv("ADMIN_NAME", "admin"),
        "username": os.getenv("ADMIN_USER", "admin"),
        "user_email": os.getenv("ADMIN_EMAIL", "admin@admin.com"),
        "password": os.getenv("ADMIN_PASSWORD", "admin"),
    }
