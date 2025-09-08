from fastapi import FastAPI

from blog.router import authentication
from .database import engine
from . import models
from .router import blog,user
app=FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
