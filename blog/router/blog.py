from fastapi import APIRouter,Depends,HTTPException,status
from .. import models,schemas,database,models
from typing import List
from sqlalchemy.orm import Session
router=APIRouter(
    tags=['blogs'],
    prefix="/blog"
)

@router.get('/',response_model=List[schemas.ShowBlog])
def get_all_blogs(db:Session=Depends(database.get_db)):
    blogs=db.query(models.Blog).all()
    return blogs


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog,db:Session=Depends(database.get_db)):
    new_blog=models.Blog(title=blog.title,body=blog.body,published=blog.published,author=blog.author,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog,tags=['blogs'])
def get_blog(id, db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # return Response(status_code=status.HTTP_404_NOT_FOUND)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} not available')
    return blog


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,db:Session=Depends(database.get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete()
    db.commit()
    return {'blog deleted successfully'}

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,blog:schemas.Blog,db:Session=Depends(database.get_db)):

    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} not available')
    blog.update({'title':blog.title,'body':blog.body})
    db.commit()
    return {'blog updated successfully'}

