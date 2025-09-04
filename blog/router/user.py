from fastapi import APIRouter,Depends,HTTPException,status
from .. import models,schemas,database,models
from typing import List
from sqlalchemy.orm import Session
from .. import hashing
from ..hashing import Hash
router=APIRouter(
    tags=['Users'],
    prefix="/user"
)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(user:schemas.User,db:Session=Depends(database.get_db)):
    new_user=models.User(name=user.name,email=user.email,password=Hash.hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id,db:Session=Depends(database.get_db)):
   user=db.query(models.User).filter(models.User.id==id).first()
   if not user:
       raise HTTPException(status_code=404,detail=f'User with the id {id} not available')
   
   return user
