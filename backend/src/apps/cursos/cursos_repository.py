# Dependency
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Packages
from . import CursosModel
from src.database.base import Base

# Exceptions
from src.exceptions.process_error import (
    UniqueConstraintViolationException,
    EntityNotFoundException,
)
from sqlalchemy.exc import IntegrityError


class CursosRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save(self, entity_model: CursosModel) -> CursosModel:
        try:
            self.session.add(entity_model)
            self.session.commit()
            return entity_model

        except IntegrityError as err:
            self.session.rollback()
            raise UniqueConstraintViolationException(err)

        except Exception as err:
            self.session.rollback()
            print(type(err))
            print(err)

    def find_all(self) -> list[CursosModel]:
        query = self.session.query(CursosModel)
        result = query.all()

        return result

    def find(self, _id: int = None, _externalId: str = None) -> CursosModel | None:

        query = self.session.query(CursosModel)
        result: Optional[CursosModel] = None

        if _externalId is None:
            result = query.filter_by(id=_id).first()
        else:
            result = query.filter(CursosModel.externalId == _externalId).first()

        if result is None:
            raise EntityNotFoundException("Curso não encontrado!")

        return result

    def edit(self, _id: int, entity_model: CursosModel) -> CursosModel | None:
        newEntity = self.session.query(CursosModel).filter_by(id=_id).first()

        if newEntity is None:
            raise EntityNotFoundException("Curso não encontrado!")

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

        if resultEntity is None:
            raise EntityNotFoundException("Curso não encontrado!")

        self.session.delete(resultEntity)
        self.session.commit()
        return resultEntity
