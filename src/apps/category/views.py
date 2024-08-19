from typing import Annotated
import logging

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.schemas import CreateCategory, Category
from src.apps.category import crud
from src.db import db_helper

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/category_list", response_model=Category | list)
async def category_list(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ]
):
    """
    Get list of categories.
    """
    # TODO: Implement logic to get categories from database
    categories = await crud.get_categories_obj(session)
    return [Category.from_orm(category) for category in categories]


# @router.post("/category_create", response_model=CreateCategory)
# async def category_create(
#         session: Annotated[
#             AsyncSession,
#             Depends(db_helper.session_getter),
#         ],
#         category_data: CreateCategory
# ):
#     """
#     Get list of categories.
#     """
#     # TODO: Implement logic to get categories from database
#
#     return await crud.create_category_obj(session, category_data.dict())
