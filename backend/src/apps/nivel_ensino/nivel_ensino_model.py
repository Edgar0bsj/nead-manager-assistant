from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.database.base import Base
from src.database.timestamp_mixin import TimestampMixin


class NivelEnsinoModel(TimestampMixin, Base):
    __tablename__ = "nivel_ensino"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    sistema: Mapped[str] = mapped_column(String(100))
    unidade: Mapped[str] = mapped_column(String(100))
    # -----------------

    name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(100))

    educationLevelTypeId: Mapped[str] = mapped_column(String(25))
