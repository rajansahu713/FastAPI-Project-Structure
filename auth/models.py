from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    email: str
    hashed_password: str

# In-memory "database"
fake_users_db: List[User] = []
blocklist_token =[]



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
    def __repr__(self):
        return 'UserModel(username=%s, email_id=%s)' % (self.username, self.email_id)
    
class BlockToken(Base):
    __tablename__ = "Blocktokens"
    id = Column(Integer, primary_key = True)
    token = Column(String(200), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    
    
# class Item(Base):
#     __tablename__ = "items"
    
#     id = Column(Integer, primary_key=True,index=True)
#     name = Column(String(80), nullable=False, unique=True,index=True)
#     price = Column(Float(precision=2), nullable=False)
#     description = Column(String(200))
#     store_id = Column(Integer,ForeignKey('stores.id'),nullable=False)
#     def __repr__(self):
#         return 'ItemModel(name=%s, price=%s,store_id=%s)' % (self.name, self.price,self.store_id)
    
# class Store(Base):
#     __tablename__ = "stores"
#     id = Column(Integer, primary_key=True,index=True)
#     name = Column(String(80), nullable=False, unique=True)
#     items = relationship("Item",primaryjoin="Store.id == Item.store_id",cascade="all, delete-orphan")

#     def __repr__(self):
#         return 'Store(name=%s)' % self.name