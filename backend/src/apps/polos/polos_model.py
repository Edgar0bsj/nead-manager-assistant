# Dependency
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Packages
from src.database import TimestampMixin, Base


class PoloModel(TimestampMixin, Base):
    __tablename__ = "polos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(100))

    cursos: Mapped[list["CursosModel"]] = relationship(  # type: ignore
        back_populates="polo", lazy="selectin"
    )
