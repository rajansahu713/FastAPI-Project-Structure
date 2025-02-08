from fastapi import APIRouter

from apps.blogs import controller as blog_controller
from apps.events import controller as event_controller
from auth import controller as auth_controller
from common import constants

main_router = APIRouter()

main_router.include_router(
    router=blog_controller.blog_router, prefix="/blogs", tags=[constants.BLOGS]
)
main_router.include_router(
    router=auth_controller.auth_router, prefix="/auth", tags=[constants.AUTH]
)

main_router.include_router(
    router=event_controller.event_router, prefix="/events", tags=[constants.EVENTS]
)
