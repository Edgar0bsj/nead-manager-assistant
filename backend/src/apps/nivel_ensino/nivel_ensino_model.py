# Dependency
from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Packages
from src.database import Base, TimestampMixin

# Relationship
# from src.apps.cursos.cursos_model import CursosModel


class NivelEnsinoModel(TimestampMixin, Base):
    __tablename__ = "nivel_ensino"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    status: Mapped[bool] = mapped_column(Boolean, default=True)

    name: Mapped[str] = mapped_column(String(100))

    externalId: Mapped[str] = mapped_column(String(100), unique=True)

    educationLevelTypeId: Mapped[str] = mapped_column(String(100))

    cursos: Mapped[list["CursosModel"]] = relationship(back_populates="nivel_ensino", lazy="selectin")  # type: ignore
