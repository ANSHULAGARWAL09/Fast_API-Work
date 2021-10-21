from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.Project_Title, version=settings.Project_Version)

@app.get("/")
def hello_api():
    return{"detail":"Hello World!"}