from fastapi import FastAPI
import src.controllers.freteController as controller
from src.database import database

app = FastAPI()
controller.resource(app,database.mySession())


