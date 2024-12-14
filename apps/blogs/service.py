from apps.blogs.data import create_blog, delete_blog, get_blog, update_blog
from apps.blogs.schemas import BlogCreate


async def create_blog_service(db, blog, user_id):
    return await create_blog(db, blog, user_id)


async def get_blog_service(db, blog_id):
    return await get_blog(db, blog_id)


async def update_blog_service(db, blog_id: int, blog: BlogCreate):
    return await update_blog(db, blog_id, blog)


async def delete_blog_service(db, blog_id: int):
    return await delete_blog(db, blog_id)
