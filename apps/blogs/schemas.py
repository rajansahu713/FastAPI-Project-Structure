from pydantic import BaseModel, EmailStr

class BlogCreate(BaseModel):
    title : str
    description : str
    