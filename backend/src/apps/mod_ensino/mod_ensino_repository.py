from typing import Optional

from src.err.exceptios import EntityNotFoundException
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.apps.mod_ensino.mod_ensino_model import ModEnsinoModel


class ModEnsinoRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save(self, entity_model: ModEnsinoModel) -> ModEnsinoModel:
        self.session.add(entity_model)
        self.session.commit()
        return entity_model

    def find_all(self, filter_status: Optional[bool] = None) -> list[ModEnsinoModel]:

        query = self.session.query(ModEnsinoModel)

        if filter_status is not None:
            query = query.filter(ModEnsinoModel.status == True)

        result = query.all()

        return result

    def find(self, _id: int) -> ModEnsinoModel | None:
        result = self.session.query(ModEnsinoModel).filter_by(id=_id).first()
        if result is None:
            raise EntityNotFoundException()
        return result

    def edit(self, _id: int, entity_model: ModEnsinoModel) -> ModEnsinoModel | None:
        newEntity = self.session.query(ModEnsinoModel).filter_by(id=_id).first()

        newEntity.status = entity_model.status
        newEntity.name = entity_model.name
        newEntity.externalId = entity_model.externalId
        newEntity.teachingModalityTypeId = entity_model.teachingModalityTypeId

        self.session.commit()
        return newEntity

    def remove(self, _id: int) -> ModEnsinoModel | None:
        resultEntity = self.session.query(ModEnsinoModel).filter_by(id=_id).first()
        self.session.delete(resultEntity)
        self.session.commit()
        return resultEntity
