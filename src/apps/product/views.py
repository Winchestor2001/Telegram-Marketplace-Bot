from fastapi import APIRouter
from src.apps.schemas import Product, CreateProduct

router = APIRouter()


@router.get("/product_list", response_model=Product)
async def product_list():
    """
    Get list of products.

    :return: list of products.
    """
    # TODO: Implement logic to get products from database
    return []


@router.post("/product_create", response_model=CreateProduct)
async def product_create():
    """
    Get list of products.

    :return: list of products.
    """
    # TODO: Implement logic to get products from database
    return []
