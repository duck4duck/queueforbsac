from fastapi import APIRouter

from .crud.managers import ws_router


router = APIRouter()
router.include_router(ws_router)
