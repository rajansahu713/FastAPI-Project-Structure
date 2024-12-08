from fastapi import APIRouter, Depends
from auth.auth import AuthHandler

blog_router = APIRouter()

auth_handle = AuthHandler()



@blog_router.get("/")
async def root(user = Depends(auth_handle.auth_wrapper)):
    return {"message": "Hello World"}