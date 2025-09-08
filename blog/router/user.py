from fastapi import APIRouter,Depends,status
from .. import schemas,database
from typing import List
from sqlalchemy.orm import Session
from ..repository import user as user_repository
router=APIRouter(
    tags=['Users'],
    prefix="/user"
)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(user:schemas.User,db:Session=Depends(database.get_db)):
   return user_repository.create(user,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id,db:Session=Depends(database.get_db)):
  return user_repository.show_user(id,db)
