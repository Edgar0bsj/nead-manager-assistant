from datetime import date

from sqlalchemy.sql import func
from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.apps.alt_codigo_externo.alt_codigo_externo_model import (
    AlteracaoCodigoExternoModel,
)


class AlteracaoCodigoExternoRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save(
        self, entity_model: AlteracaoCodigoExternoModel
    ) -> AlteracaoCodigoExternoModel:
        self.session.add(entity_model)
        self.session.commit()
        return entity_model

    def find_all(self) -> list[AlteracaoCodigoExternoModel]:
        # return self.session.query(AlteracaoCodigoExternoModel).all()
        return (
            self.session.query(AlteracaoCodigoExternoModel)
            .filter(AlteracaoCodigoExternoModel.deleted_at.is_(None))
            .all()
        )

    def find(self, _id: int) -> AlteracaoCodigoExternoModel | None:
        return self.session.query(AlteracaoCodigoExternoModel).filter_by(id=_id).first()

    def edit(
        self, _id: int, entity_model: AlteracaoCodigoExternoModel
    ) -> AlteracaoCodigoExternoModel | None:
        newEntity = (
            self.session.query(AlteracaoCodigoExternoModel).filter_by(id=_id).first()
        )
        newEntity.status = entity_model.status
        newEntity.sistema = entity_model.sistema
        newEntity.unidade = entity_model.unidade
        newEntity.entity = entity_model.entity
        newEntity.oldExternalId = entity_model.oldExternalId
        newEntity.newExternalId = entity_model.newExternalId

        self.session.commit()
        return newEntity

    def remove(self, _id: int) -> AlteracaoCodigoExternoModel | None:
        resultEntity = (
            self.session.query(AlteracaoCodigoExternoModel).filter_by(id=_id).first()
        )
        resultEntity.status = False
        resultEntity.deleted_at = func.now()
        # self.session.delete(resultEntity)
        self.session.commit()
        return resultEntity

    def find_all_by_ativo(self):
        return (
            self.session.query(AlteracaoCodigoExternoModel)
            .filter(AlteracaoCodigoExternoModel.deleted_at.is_(None))
            .filter(AlteracaoCodigoExternoModel.status == True)
            .all()
        )
