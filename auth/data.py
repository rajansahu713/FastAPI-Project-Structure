from sqlalchemy.orm import Session

from auth.models import BlockToken, User
from auth.schemas import UserCreate


async def create_user(db: Session, user: UserCreate):
    db_item = User(
        username=user.username,
        mobile_no=user.mobile_no,
        email_id=user.email_id,
        password=user.password,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def get_user_details(db: Session, username):
    user = db.query(User).filter(User.username == username)
    if user:
        return user.first()
    return None


async def block_token(token, db: Session):
    db_item = BlockToken(token=token)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def is_token_blocked(db: Session, token):
    token = db.query(BlockToken).filter(BlockToken.token == token).first()
    if token:
        return True
    return False
