from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.db import Base

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(80), nullable=False, unique=True,index=True)
    description = Column(String(200))
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    def __repr__(self):
        return 'BlogModel(title=%s, user_id=%s)' % (self.title, self.user_id)
    