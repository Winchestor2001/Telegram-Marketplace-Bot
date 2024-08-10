from fastapi.routing import APIRouter
from src.settings import settings
# from src.apps.api.docs.views import router as docs_router

api_router = APIRouter(prefix=settings.api.prefix)

# api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
