from typing import Optional

from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.err.exceptios import EntityNotFoundException
from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker

from src.apps.cursos.cursos_model import CursosModel


class CursosRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save(self, entity_model: CursosModel) -> CursosModel:
        self.session.add(entity_model)
        self.session.commit()
        return entity_model

    def find_all(self) -> list[CursosModel]:
        query = self.session.query(CursosModel)
        result = query.all()

        return result

    def find(self, _id: int) -> CursosModel | None:
        result = self.session.query(CursosModel).filter_by(id=_id).first()
        if result is None:
            raise EntityNotFoundException()
        return result

    def edit(self, _id: int, entity_model: CursosModel) -> CursosModel | None:
        newEntity = self.session.query(CursosModel).filter_by(id=_id).first()

        newEntity.name = entity_model.name
        newEntity.externalId = entity_model.externalId
        newEntity.isActive = entity_model.isActive
        newEntity.externalTeachingModalityId = entity_model.externalTeachingModalityId
        newEntity.externalEducationLevelId = entity_model.externalEducationLevelId
        newEntity.courseTypeId = entity_model.courseTypeId
        newEntity.polo_id = entity_model.polo_id

        self.session.commit()
        return newEntity

    def remove(self, _id: int) -> CursosModel | None:
        resultEntity = self.session.query(CursosModel).filter_by(id=_id).first()
        self.session.delete(resultEntity)
        self.session.commit()
        return resultEntity
