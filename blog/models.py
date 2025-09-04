from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base() 
class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    published=Column(Boolean,default=True)
    author=Column(String,nullable=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship('User',back_populates="blogs")


class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    blogs=relationship('Blog',back_populates="user")

# this is sql alchemy model