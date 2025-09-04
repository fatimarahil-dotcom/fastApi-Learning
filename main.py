from fastapi import FastAPI
from . import models
from . import schemas
app=FastAPI()

models.base.metadata.create_all(bind=models.engine)

@app.get('/')
def index():
    return {"message":"Hello, World!"}

@app.post('/blog')
def create_blog(blog: Blog):
    return {"message": "Blog created successfully", "blog": blog}