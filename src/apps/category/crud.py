from typing import List, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.category import Category
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload


async def create_category_obj(session: AsyncSession, data: dict) -> Category:
    category = Category(**data)
    session.add(category)
    await session.commit()
    return category


async def get_categories_obj(session: AsyncSession) -> Sequence[Category]:
    categories = select(Category).where(Category.obj_state == 1)
    result = await session.execute(categories)
    return result.scalars().all()

