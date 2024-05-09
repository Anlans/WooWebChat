from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # 定义连接异步引擎数据库的URL地址
    ASYNC_DATABASE_URI: str = "sqlite+aiosqlite:///chat.db"
    # 定义TOKEN的签名信息
    # TOKEN_SIGN_SECRET: str = "sdlfhosidghosj"

@lru_cache()
def get_setting():
    return Settings()
