from fastapi import APIRouter,Depends,status
from blog.oauth2 import get_current_user
from .. import models,schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog as blog_repository
router=APIRouter(
    tags=['blogs'],
    prefix="/blog"
)

@router.get('/',response_model=List[schemas.ShowBlog])
def get_all_blogs(db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blog_repository.get_all(db)
    


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog,db:Session=Depends(database.get_db),current_user: schemas.TokenData = Depends(get_current_user)):
    return blog_repository.create_blog(blog,db,current_user)

@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog,tags=['blogs'])
def get_blog(id, db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(get_current_user)):
   return blog_repository.show(id,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blog_repository.delete_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,blog:schemas.Blog,db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blog_repository.update(id,blog,db)

