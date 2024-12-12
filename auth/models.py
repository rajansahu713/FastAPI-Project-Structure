from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import datetime

from database.db import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,index=True)
    email_id = Column(String(80), nullable=False, unique=True,index=True)
    mobile_no = Column(String(80), nullable=False, unique=True,index=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return 'UserModel(username=%s, email_id=%s)' % (self.username, self.email_id)
    
class BlockToken(Base):
    __tablename__ = "Blocktokens"
    id = Column(Integer, primary_key = True)
    token = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
