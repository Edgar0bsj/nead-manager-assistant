from sqlalchemy import Boolean, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base
from src.database.timestamp_mixin import TimestampMixin


class CursosModel(TimestampMixin, Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    sistema: Mapped[str] = mapped_column(String(100))
    unidade: Mapped[str] = mapped_column(String(100))
    # -----------------

    name: Mapped[str] = mapped_column(String(150))

    externalId: Mapped[str] = mapped_column(String(100), unique=True)

    isActive: Mapped[bool] = mapped_column(Boolean)

    externalTeachingModalityId: Mapped[str] = mapped_column(
        ForeignKey("modalidades_ensino.externalId")
    )

    externalEducationLevelId: Mapped[str] = mapped_column(
        ForeignKey("nivel_ensino.externalId")
    )

    courseTypeId: Mapped[str] = mapped_column(String(100))

    mod_ensino: Mapped[list["ModEnsinoModel"]] = relationship(  # type: ignore
        back_populates="cursos"
    )
    nivel_ensino: Mapped[list["NivelEnsinoModel"]] = relationship(  # type: ignore
        back_populates="cursos"
    )
