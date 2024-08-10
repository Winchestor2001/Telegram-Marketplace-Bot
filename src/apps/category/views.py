from fastapi import APIRouter
from src.apps.schemas import CreateCategory, Category

router = APIRouter()


@router.get("/category_list", response_model=Category)
async def category_list():
    """
    Get list of categories.

    :return: list of categories.
    """
    # TODO: Implement logic to get categories from database
    return []


@router.post("/category_create", response_model=CreateCategory)
async def category_create():
    """
    Get list of categories.

    :return: list of categories.
    """
    # TODO: Implement logic to get categories from database
    return []
