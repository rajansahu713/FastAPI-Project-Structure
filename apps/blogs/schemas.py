from pydantic import BaseModel


class BlogCreate(BaseModel):
    title: str
    description: str
