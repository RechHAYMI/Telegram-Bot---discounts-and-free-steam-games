from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine("postgresql+asyncpg://admin:my_secret_password@localhost:5433/discount_db")

async_session = async_sessionmaker(engine, expire_on_commit=False)