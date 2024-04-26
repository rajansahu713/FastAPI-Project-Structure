from fastapi import FastAPI, Depends
from common import constants as global_constant
from common import helper_function as global_helper
from routers import main_router


app = FastAPI(
    title=global_constant.TITLE_TAGS,
    Prefix=f"/{global_constant.PREFIX}",
    docs_url=f"/{global_constant.PREFIX}/docs",
    redocs=f"/{global_constant.PREFIX}/redocs",
    version=global_constant.VERSION,
    description=global_constant.DESCRIPTIONS,
    dependencies=[Depends(global_helper.check_maintenance)],
)

app.include_router(main_router)



    