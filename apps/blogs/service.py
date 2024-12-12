from apps.blogs.data import create_blog

async def create_blog_service(db, blog, user_id):
    return await create_blog(db, blog, user_id)