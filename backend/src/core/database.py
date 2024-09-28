import peewee
from .config import Config

# Mapping of database types to their respective Peewee classes
DATABASES = {
    "postgres": peewee.PostgresqlDatabase,
    "sqlite": peewee.SqliteDatabase,
    "mysql": peewee.MySQLDatabase,
}


# Function to get the database configuration
def get_database():
    db_type = Config.DB["database"]
    if db_type not in DATABASES:
        raise ValueError("Unsupported database type")

    db_class = DATABASES[db_type]

    # If the database type is sqlite, no need to pass user and password
    if db_type == "sqlite":
        return db_class(Config.DB["database"])

    # Otherwise, we pass user and password
    return db_class(
        Config.DB["database"],
        user=Config.DB["user"],
        password=Config.DB["password"],
        host=Config.DB["host"],
        port=Config.DB["port"],
    )


# Get the database instance
db = get_database()


# Base model class
class BaseModel(peewee.Model):
    class Meta:
        database = db
