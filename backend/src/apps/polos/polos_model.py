from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base
from src.database.timestamp_mixin import TimestampMixin


class PoloModel(TimestampMixin, Base):
    __tablename__ = "polos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(100))

    cursos: Mapped[list["CursosModel"]] = relationship(  # type: ignore
        back_populates="polo", lazy="selectin"
    )
