from .config import Config
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt

error_token = {
    "error": "Invalid token",
    "message": "O token fornecido é inválido.",
}


class Security:
    secret = Config.SECRET_KEY
    algorithm = "HS256"
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    default_expires_delta = timedelta(days=1)

    # Criptografar senha
    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    # Verificar senha
    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(password, hashed_password)

    # Criar token JWT com tempo de expiração customizável
    @classmethod
    def create_jwt(cls, data: dict, expires: timedelta | None = None) -> str:
        to_encode = data.copy()
        if not expires:
            expires = cls.default_expires_delta
        expire = datetime.now(timezone.utc) + expires
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, cls.secret, algorithm=cls.algorithm)

    # Decodificar token JWT
    @classmethod
    def decode_jwt(cls, token: str) -> dict:
        try:
            payload = jwt.decode(token, cls.secret, algorithms=[cls.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return error_token
        except jwt.InvalidTokenError:
            return error_token
