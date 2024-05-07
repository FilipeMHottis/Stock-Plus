from dotenv import load_dotenv
import os

load_dotenv()

database = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "1234"),
    "dbname": os.getenv("DB_NAME", "stock"),
}
