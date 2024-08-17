import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.apps.product.utils import base64_image_saver
from src.apps.schemas import Product, CreateProduct, FilterProduct
from src.apps.product import crud
from src.db import db_helper
import logging

router = APIRouter()
logger = logging.getLogger('fastapi_app')


@router.get("/product_list", response_model=Product | list)
async def product_list(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        filter_data: FilterProduct = Depends()
):
    """
    Get list of products.
    """
    # TODO: Implement logic to get products from database
    products = await crud.get_products_obj(session, filter_data)
    return [Product.from_orm(product) for product in products]


@router.post("/product_create", response_model=Product)
async def product_create(
        request: Request,
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

    product_uuid = str(uuid.uuid4())
    product_data = product_data.dict()
    product_data['uuid'] = product_uuid
    product_images = product_data.pop('images')
    new_product = await crud.create_product_obj(session, product_data)

    if not new_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Foreign key is wrong")

    domain = str(request.base_url)
    for img in product_images:
        image = await base64_image_saver(
            img_folder="products", image_base64=img, base_url=domain, uuid=new_product.uuid
        )
        product_image = {"image": image, "product_uuid": new_product.uuid}
        await crud.add_product_image_obj(session, product_image)

    product = await crud.get_product_obj(session, new_product.uuid)

    return product
