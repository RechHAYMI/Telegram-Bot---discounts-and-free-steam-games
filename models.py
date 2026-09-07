from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Boolean, Float

class Base(DeclarativeBase): 
    pass

class Game(Base):
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(primary_key=True)
    steam_id: Mapped[int] = mapped_column(Integer, unique=True)
    title: Mapped[str] = mapped_column(String)
    discount_percent: Mapped[int] = mapped_column(Integer)
    url: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    price_rub: Mapped[float] = mapped_column(Float)
    price_kzt: Mapped[float] = mapped_column(Float)
    price_usd: Mapped[float] = mapped_column(Float)
    price_uah: Mapped[float] = mapped_column(Float)