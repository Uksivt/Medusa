from fastapi import APIRouter
from .groups.views import router as groups_router
from .search.views import router as search_router

router = APIRouter()
router.include_router(router=groups_router, prefix="/groups")
router.include_router(router=search_router, prefix="/search")
