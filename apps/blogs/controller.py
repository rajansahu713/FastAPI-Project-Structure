from fastapi import APIRouter

blog_router = APIRouter()


@blog_router.get("/")
async def root():
    return {"message": "Hello World"}