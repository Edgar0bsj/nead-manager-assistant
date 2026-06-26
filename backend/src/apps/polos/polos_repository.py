# Dependency
from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker

# Packages
from .polos_model import PoloModel

# Exceptions
from src.exceptions import EntityNotFoundException
from sqlalchemy.exc import IntegrityError
from src.exceptions import RecordHasDependenciesException


class PoloRepository:

    def __init__(self, url_db="sqlite:///src/database/database.db") -> None:
        self.engine = create_engine(url_db)

        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save(self, entity_model: PoloModel) -> PoloModel:
        self.session.add(entity_model)
        self.session.commit()
        return entity_model

    def find_all(self) -> list[PoloModel]:

        query = self.session.query(PoloModel)

        result = query.all()

        return result

    def find(self, _id: int) -> PoloModel | None:

        result = self.session.query(PoloModel).filter_by(id=_id).first()

        if result is None:
            raise EntityNotFoundException("Polo não encontrado!")

        return result

    def edit(self, _id: int, entity_model: PoloModel) -> PoloModel | None:
        newEntity = self.session.query(PoloModel).filter_by(id=_id).first()

        if newEntity is None:
            raise EntityNotFoundException("Polo não encontrado!")

        newEntity.name = entity_model.name

        self.session.commit()
        return newEntity

    def remove(self, _id: int) -> PoloModel | None:
        try:
            resultEntity = self.session.query(PoloModel).filter_by(id=_id).first()

            if resultEntity is None:
                raise EntityNotFoundException("Polo não encontrado!")

            self.session.delete(resultEntity)
            self.session.commit()
            return resultEntity

        except IntegrityError:
            raise RecordHasDependenciesException(
                "Não é possível deletar o polo porque ele possui vinculados."
            )
