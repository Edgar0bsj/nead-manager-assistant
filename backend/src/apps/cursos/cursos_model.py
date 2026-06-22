from sqlalchemy import Boolean, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base
from src.database.timestamp_mixin import TimestampMixin

# Relacionamento _______________
from src.apps.mod_ensino.mod_ensino_model import ModEnsinoModel
from src.apps.nivel_ensino.nivel_ensino_model import NivelEnsinoModel


class CursosModel(TimestampMixin, Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(150))

    externalId: Mapped[str] = mapped_column(String(50), unique=True)

    isActive: Mapped[bool] = mapped_column(Boolean)

    externalTeachingModalityId: Mapped[str] = mapped_column(
        ForeignKey("modalidades_ensino.externalId")
    )

    externalEducationLevelId: Mapped[str] = mapped_column(
        ForeignKey("nivel_ensino.externalId")
    )

    courseTypeId: Mapped[str] = mapped_column(String(20))

    modalidade_ensino: Mapped["ModEnsinoModel"] = relationship(
        back_populates="cursos", lazy="selectin"
    )
    nivel_ensino: Mapped["NivelEnsinoModel"] = relationship(
        back_populates="cursos", lazy="selectin"
    )
