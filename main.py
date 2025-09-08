from fastapi import FastAPI
from . import models
from . import schemas
app=FastAPI()

models.base.metadata.create_all(bind=models.engine)

@app.get('/')
def index():
    return {"message":"Hello, World!"}
