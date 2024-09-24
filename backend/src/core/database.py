import peewee
from config import Config

# Mapeamento de tipos de banco de dados para as respectivas classes Peewee
DATABASES = {
    "postgres": peewee.PostgresqlDatabase,
    "sqlite": peewee.SqliteDatabase,
    "mysql": peewee.MySQLDatabase,
}


# Função para obter a configuração do banco de dados
def get_database():
    db_type = Config.DB["database"]
    if db_type not in DATABASES:
        raise ValueError("Unsupported database type")

    db_class = DATABASES[db_type]

    # Caso seja um sqlite, não é necessário passar usuário e senha
    if db_type == "sqlite":
        return db_class(Config.DB["database"])

    # Caso contrário, passamos usuário e senha
    return db_class(
        Config.DB["database"],
        user=Config.DB["user"],
        password=Config.DB["password"],
        host=Config.DB["host"],
        port=Config.DB["port"],
    )


# Obter a instância do banco de dados
db = get_database()


# Modelo base
class BaseModel(peewee.Model):
    class Meta:
        database = db
