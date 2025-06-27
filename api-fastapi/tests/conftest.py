import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.database import DataBase




#Sempre que eu tiver um metodo de teste que recebe um client
# ele recebera essa função como parametro
@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():

    database = DataBase('sqlite:///:memory:')
    database.migration()
    
    with database.mySession() as session:
        yield session

    database.drop()
    

    