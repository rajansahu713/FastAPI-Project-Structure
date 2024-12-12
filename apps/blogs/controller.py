from fastapi import APIRouter, Depends
from auth.auth import AuthHandler
from apps.blogs.schemas import BlogCreate
from apps.blogs.service import create_blog_service
from database.db import get_db
from sqlalchemy.orm import Session


blog_router = APIRouter()

auth_handle = AuthHandler()



@blog_router.get("/blogs")
async def root(user = Depends(auth_handle.auth_wrapper)):
    try:
        return {"message": "Hello World"}
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}
    

@blog_router.post("/blogs")
async def root(blog: BlogCreate,user = Depends(auth_handle.auth_wrapper), db: Session = Depends(get_db)):
    try:
        await create_blog_service(db, blog, user.id)
        return {"message": "Blog created successfully"}
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}
    
@blog_router.get("/blogs/{id}")
async def root(id: int, user = Depends(auth_handle.auth_wrapper)):
    try:
        return {"message": "Hello World"}
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}

@blog_router.put("/blogs/{id}")
async def root(id: int, user = Depends(auth_handle.auth_wrapper)):
    try:
        return {"message": "Hello World"}
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}
    

@blog_router.delete("/blogs/{id}")
async def root(id: int, user = Depends(auth_handle.auth_wrapper)):
    try:
        return {"message": "Hello World"}
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}