from fastapi import APIRouter, Depends
from auth.auth import AuthHandler
from apps.blogs.schemas import BlogCreate
from apps.blogs.service import create_blog_service, get_blog_service, update_blog_service, delete_blog_service
from database.db import get_db
from sqlalchemy.orm import Session

blog_router = APIRouter()
auth_handle = AuthHandler()


@blog_router.get("/")
async def root(_= Depends(auth_handle.auth_wrapper), blog_id: int=None, db: Session = Depends(get_db)):
    try:
        return await get_blog_service(db,blog_id)
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}
    

@blog_router.post("")
async def root(blog: BlogCreate,user = Depends(auth_handle.auth_wrapper), db: Session = Depends(get_db)):
    try:
        await create_blog_service(db, blog, user.id)
        return {"message": "Blog created successfully"}
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}
    

@blog_router.put("/")
async def root(blog_id: int, blog: BlogCreate, user = Depends(auth_handle.auth_wrapper), db: Session = Depends(get_db)):
    try:
        return await update_blog_service(db, blog_id, blog)
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}
    

@blog_router.delete("/")
async def root(blog_id: int, user = Depends(auth_handle.auth_wrapper), db: Session = Depends(get_db)):
    try:
        return await delete_blog_service(db,blog_id)
    except Exception as err:
        return {"error": "Due to this error {}".format(err)}