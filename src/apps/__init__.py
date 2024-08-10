from fastapi.routing import APIRouter
from src.settings import settings
from src.apps.docs.views import router as docs_router
from src.apps.category.views import router as category_router
from src.apps.product.views import router as product_router

api_router = APIRouter(prefix=settings.api.prefix)

api_router.include_router(docs_router)
api_router.include_router(category_router, prefix="/category", tags=["Category"])
api_router.include_router(product_router, prefix="/product", tags=["Product"])
