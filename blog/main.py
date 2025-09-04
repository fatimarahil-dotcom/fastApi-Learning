from fastapi import FastAPI,Depends,status,HTTPException
from .database import engine,session
from . import models,schemas
from sqlalchemy.orm import Session 
from typing import List
app=FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=blog.title,body=blog.body,published=blog.published,author=blog.author)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
@app.get('/blog',response_model=List[schemas.ShowBlog])
def get_all_blogs(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def get_blog(id, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # return Response(status_code=status.HTTP_404_NOT_FOUND)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} not available')
    return blog

# can also raise http exception instead of returning response

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,db:Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete()
    db.commit()
    return {'blog deleted successfully'}

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,blog:schemas.Blog,db:Session=Depends(get_db)):

    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} not available')
    blog.update({'title':blog.title,'body':blog.body})
    db.commit()
    return {'blog updated successfully'}


    
