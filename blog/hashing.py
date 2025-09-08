
from passlib.context import CryptContext
class Hash:
    pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls,password:str):
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls,hashed_password,plain_password)->bool:
        return cls.pwd_context.verify(plain_password,hashed_password)
