from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from src.apps.product.utils import filter_obj
from src.db import Product, ProductImage
import logging

logger = logging.getLogger('fastapi_app')


async def create_product_obj(session: AsyncSession, data: dict) -> Product | bool:
    product = Product(**data)
    session.add(product)
    try:
        await session.commit()
    except IntegrityError as e:
        return False
    return product


async def get_product_obj(session: AsyncSession, product_uuid: str) -> Product:
    product = select(Product).where(Product.uuid == product_uuid).options(
        selectinload(Product.category),
        selectinload(Product.images))
    result = await session.execute(product)
    return result.scalars().first()


async def add_product_image_obj(session: AsyncSession, data: dict) -> ProductImage | bool:
    product_image = ProductImage(**data)
    session.add(product_image)
    try:
        await session.commit()
    except IntegrityError:
        return False
    return product_image


async def get_products_obj(session: AsyncSession, filter_data) -> Sequence[Product]:
    stmt = select(Product).options(selectinload(Product.category), selectinload(Product.images))
    products = await filter_obj(stmt, filter_data, Product)
    result = await session.execute(products)

    return result.scalars().all()
