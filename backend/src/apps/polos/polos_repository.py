from src.err.exceptios import EntityNotFoundException
from sqlalchemy import create_engine
from src.database.base import Base
from sqlalchemy.orm import sessionmaker
from src.apps.polos.polos_model import PoloModel


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
            raise EntityNotFoundException()
        return result

    def edit(self, _id: int, entity_model: PoloModel) -> PoloModel | None:
        newEntity = self.session.query(PoloModel).filter_by(id=_id).first()
        newEntity.name = entity_model.name

        self.session.commit()
        return newEntity

    def remove(self, _id: int) -> PoloModel | None:
        resultEntity = self.session.query(PoloModel).filter_by(id=_id).first()

        self.session.delete(resultEntity)
        self.session.commit()
        return resultEntity
