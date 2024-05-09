from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from config.config import get_setting

# 创建异步数据库引擎
async_engine = create_async_engine(get_setting().ASYNC_DATABASE_URI, echo=False)

# 创建基类
Base = declarative_base()

# 通过异步数据库引擎创建异步的会话管理对象
SessionLocal = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)
