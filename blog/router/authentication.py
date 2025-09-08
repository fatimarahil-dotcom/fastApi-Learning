from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog import models
from blog.hashing import Hash
from .. import schemas,database,token
router=APIRouter(
    tags=['Authentication'],
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=404,detail='Invalid Credentials')
    if not Hash.verify_password(user.password,request.password):
        raise HTTPException(status_code=404,detail='Invalid Credentials')
    # generate a jwt token and return it

    access_token = token.create_access_token(
        data={"sub":str(user.id)}
    )
    return {"access_token": access_token, "token_type": "bearer"}