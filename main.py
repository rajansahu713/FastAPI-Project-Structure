from fastapi import FastAPI, Depends
from common import constants as global_constant
from common import helper_function as global_helper
from routers import main_router
from fastapi.middleware.cors import CORSMiddleware
from database.db import engine, Base
from auth import models
from contextlib import asynccontextmanager


app = FastAPI(
    title=global_constant.TITLE_TAGS,
    Prefix=f"/{global_constant.PREFIX}",
    docs_url=f"/{global_constant.PREFIX}/docs",
    redocs=f"/{global_constant.PREFIX}/redocs",
    version=global_constant.VERSION,
    description=global_constant.DESCRIPTIONS,
    dependencies=[Depends(global_helper.check_maintenance)],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins= global_constant.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app.include_router(main_router)



models.Base.metadata.create_all(bind=engine)

    