from fastapi import APIRouter
from apps.blogs import controller as blog_controller
main_router = APIRouter()

main_router.include_router(router=blog_controller.router, prefix="/blogs", tags=["blogs"])

