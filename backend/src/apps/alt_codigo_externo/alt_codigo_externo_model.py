from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.database.base import Base
from src.database.timestamp_mixin import TimestampMixin


class AlteracaoCodigoExternoModel(TimestampMixin, Base):
    __tablename__ = "alteracao_codigo_externo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    status: Mapped[bool] = mapped_column(Boolean, default=True)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    entity: Mapped[str] = mapped_column(String(100))

    oldExternalId: Mapped[str] = mapped_column(String(100))

    newExternalId: Mapped[str] = mapped_column(String(100))
