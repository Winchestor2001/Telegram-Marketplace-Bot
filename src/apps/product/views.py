from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.schemas import Product, CreateProduct
from src.apps.product import crud
from src.db import db_helper

router = APIRouter()


@router.get("/product_list", response_model=Product | list)
async def product_list(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ]
):
    """
    Get list of products.
    """
    # TODO: Implement logic to get products from database
    products = await crud.get_products_obj(session)
    return [Product.from_orm(product) for product in products]


@router.post("/product_create", response_model=CreateProduct)
async def product_create(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        product_data: CreateProduct
):
    """
    Get list of products.
    """
    # TODO: Implement logic to get products from database
    new_product = await crud.create_product_obj(session, product_data.dict())
    if not new_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Foreign key is wrong")
    return new_product
