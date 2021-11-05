from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app=FastAPI(title=settings.Project_Title, version=settings.Project_Version)
    create_tables()
    return app


app = start_application()

@app.get("/")
def hello_api():
    return{"detail":"Hello World!"}
