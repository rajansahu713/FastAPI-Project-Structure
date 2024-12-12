from apps.blogs.models import Blog
from sqlalchemy.orm import Session
from apps.blogs.schemas import BlogCreate

async def create_blog(db: Session, blog: BlogCreate, user_id: int):
    db_item = Blog(
        title=blog.title,
        description=blog.description,
        user_id = user_id
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    print(db_item)
    return db_item