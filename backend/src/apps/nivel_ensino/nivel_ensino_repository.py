# Dependency
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Packages
from .nivel_ensino_model import NivelEnsinoModel
from src.database import Base

# Exceptions
from src.exceptions.process_error import (
    UniqueConstraintViolationException,
    EntityNotFoundException,
)
from sqlalchemy.exc import IntegrityError


class NivelEnsinoRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save(self, entity_model: NivelEnsinoModel) -> NivelEnsinoModel:
        try:
            self.session.add(entity_model)
            self.session.commit()
            return entity_model
        except IntegrityError as err:
            raise UniqueConstraintViolationException(err)

    def find_all(self, filter_status: Optional[bool] = None) -> list[NivelEnsinoModel]:

        query = self.session.query(NivelEnsinoModel)

        if filter_status is not None:
            query = query.filter(NivelEnsinoModel.status == True)

        result = query.all()

        return result

    def find(self, _id: int) -> NivelEnsinoModel | None:
        result = self.session.query(NivelEnsinoModel).filter_by(id=_id).first()

        if result is None:
            raise EntityNotFoundException("Nivel de ensino não encontrado!")

        return result

    def edit(self, _id: int, entity_model: NivelEnsinoModel) -> NivelEnsinoModel | None:
        newEntity = self.session.query(NivelEnsinoModel).filter_by(id=_id).first()

        if newEntity is None:
            raise EntityNotFoundException("Nivel de ensino não encontrado!")

        newEntity.status = entity_model.status
        newEntity.name = entity_model.name
        newEntity.externalId = entity_model.externalId
        newEntity.educationLevelTypeId = entity_model.educationLevelTypeId

        self.session.commit()
        return newEntity

    def remove(self, _id: int) -> NivelEnsinoModel | None:
        resultEntity = self.session.query(NivelEnsinoModel).filter_by(id=_id).first()

        if resultEntity is None:
            raise EntityNotFoundException("Nivel de ensino não encontrado!")

        self.session.delete(resultEntity)
        self.session.commit()
        return resultEntity
