from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

class DataBase:

    def __init__(self, connection='sqlite:///database.db'):
        self.engine = create_engine(connection, echo=True)  # echo=True para ver o SQL gerado
        self.SessionLocal = sessionmaker(bind=self.engine, expire_on_commit=False)

    def mySession(self):
        return self.SessionLocal()
    
    def migration(self):
        Base.metadata.create_all(self.engine)
    
    def drop(self):
        Base.metadata.drop_all(self.engine)

database = DataBase()
