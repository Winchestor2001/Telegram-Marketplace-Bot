from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.db import Product


async def create_product_obj(session: AsyncSession, data: dict) -> Product | bool:
    product = Product(**data)
    session.add(product)
    try:
        await session.commit()
    except IntegrityError:
        return False
    return product


async def get_products_obj(session: AsyncSession) -> Sequence[Product]:
    products = select(Product).options(selectinload(Product.category))
    result = await session.execute(products)
    return result.scalars().all()
