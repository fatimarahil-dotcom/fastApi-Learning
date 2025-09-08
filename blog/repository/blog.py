from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session
from blog import schemas
from blog.oauth2 import get_current_user
from .. import models

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create_blog(blog:schemas.Blog,db:Session, current_user: schemas.TokenData):
    new_blog=models.Blog(title=blog.title,body=blog.body,published=blog.published,author=blog.author,user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f'Blog with the id {id} not available')
    blog.delete()
    db.commit()
    return {'blog deleted successfully'}

def update(id:int,blog:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} not available')
    blog.title = blog.title
    blog.body = blog.body
    db.commit()
    db.refresh(blog)
    return {'blog updated successfully'}

def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # return Response(status_code=status.HTTP_404_NOT_FOUND)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} not available')
    return blog