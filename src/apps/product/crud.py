from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from src.apps.product.utils import filter_obj
from src.db import Product


async def create_product_obj(session: AsyncSession, data: dict) -> Product | bool:
    product = Product(**data)
    session.add(product)
    try:
        await session.commit()
    except IntegrityError:
        return False
    return product


async def get_products_obj(session: AsyncSession, filter_data) -> Sequence[Product]:
    stmt = select(Product).options(selectinload(Product.category), selectinload(Product.images))
    products = await filter_obj(stmt, filter_data, Product)
    result = await session.execute(products)

    return result.scalars().all()
