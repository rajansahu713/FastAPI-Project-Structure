from auth.schemas import UserCreate, UserResponse, Token
from fastapi import APIRouter
from auth.auth import AuthHandler
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from auth.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Security
from auth.data import create_user
from database.db import get_db
from sqlalchemy.orm import Session


auth_router = APIRouter()
auth_handle = AuthHandler()

@auth_router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        if await auth_handle.get_user(db, user.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered",
            )
        hashed_password = await auth_handle.get_password_hash(user.password)
        user.password = hashed_password
        new_user= await create_user(db, user)
        return new_user
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Due to this error {}".format(err)
        )

@auth_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await auth_handle.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await auth_handle.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/logout")
async def logout_access_token(auth: HTTPAuthorizationCredentials = Security(auth_handle.security), db: Session = Depends(get_db)):
    await auth_handle.blocklist_token(auth.credentials, db)
    return {"message": "Logged out"}