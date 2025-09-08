from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from blog import schemas
from .. import models
from .. import hashing
from ..hashing import Hash


# def get_all(db:Session):
#     blogs=db.query(models.Blog).all()
#     return blogs


def create(user:schemas.User,db:Session):
     new_user=models.User(name=user.name,email=user.email,password=Hash.hash_password(user.password))
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return new_user

def show_user(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
       raise HTTPException(status_code=404,detail=f'User with the id {id} not available')
    return user