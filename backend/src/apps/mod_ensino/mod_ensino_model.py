from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base
from src.database.timestamp_mixin import TimestampMixin
from src.apps.cursos.cursos_model import CursosModel


class ModEnsinoModel(TimestampMixin, Base):
    __tablename__ = "modalidades_ensino"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    status: Mapped[bool] = mapped_column(Boolean, default=True)

    sistema: Mapped[str] = mapped_column(String(100))

    unidade: Mapped[str] = mapped_column(String(100))

    name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(100), unique=True)

    teachingModalityTypeId: Mapped[str] = mapped_column(String(100))

    cursos: Mapped[list["CursosModel"]] = relationship(  # type: ignore
        back_populates="mod_ensino"
    )
