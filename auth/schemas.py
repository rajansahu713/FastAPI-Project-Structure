from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    mobile_no: str
    email_id: EmailStr
    password: str


class UserResponse(BaseModel):
    username: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str
