from pydantic import BaseModel
from typing import Optional

# request model
class Blog(BaseModel):
    title: str
    body: str
    published: bool = True 
    author: Optional[str] = None  

    class Config:
        orm_mode = True   

# response model
class ShowBlog(Blog):
    pass

# this is pydantic model
