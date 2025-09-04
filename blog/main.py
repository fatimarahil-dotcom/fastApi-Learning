from fastapi import FastAPI
from .database import engine
from . import models
from .router import blog,user
app=FastAPI()

models.Base.metadata.create_all(bind=engine)


# def get_db():
#     db=session()
#     try:
#         yield db
#     finally:
#         db.close()
app.include_router(blog.router)
app.include_router(user.router)

# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
# def get_all_blogs(db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs


# can also raise http exception instead of returning response

# hash password using passlib
# place this in a seperate file
