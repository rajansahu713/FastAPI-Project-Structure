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

async def get_blog(db: Session, blog_id: int=None):
    if blog_id:
        return db.query(Blog).filter(Blog.id == blog_id).first()
    return db.query(Blog).all()

async def update_blog(db: Session, blog_id: int, blog: BlogCreate):
    db_item = db.query(Blog).filter(Blog.id == blog_id).first()
    db_item.title = blog.title
    db_item.description = blog.description
    db.commit()
    db.refresh(db_item)
    return db_item

async def delete_blog(db: Session, blog_id: int):
    print(blog_id)
    db_item = db.query(Blog).filter(Blog.id == blog_id).first()
    print(db_item)
    db.delete(db_item)
    db.commit()
    return db_item