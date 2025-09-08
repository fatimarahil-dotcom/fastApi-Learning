from pydantic import BaseModel
from typing import Optional,List

# request model

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    title: str
    body: str
    published: bool = True 
    author: Optional[str] = None  

    # by default pydantic expects a dict, 
    # and sqlAlchemy doesnt return dict, 
    # it returns object, so use this to convert
    # object to json/dict
    class Config:
        orm_mode = True   



class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog]=[]
    class Config:
        orm_mode = True  

# response model
class ShowBlog(Blog):
    user:ShowUser
    title:str
    body: str
    class Config:
        orm_mode = True 


class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None




# this is pydantic model
