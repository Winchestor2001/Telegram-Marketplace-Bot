from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.db import Profile, db_helper
import logging

logger = logging.getLogger('fastapi_app')


async def create_user_obj(username: str, telegram_id: int):
    async with db_helper.session_factory() as session:
        product = Profile(
            username=username,
            telegram_id=telegram_id
        )
        session.add(product)
        try:
            await session.commit()
        except IntegrityError as e:
            # logger.info(e)
            return False


async def get_user_info_obj(session: AsyncSession, telegram_id: int) -> Profile:
    product = select(Profile).where(Profile.telegram_id == telegram_id).options(selectinload(Profile.products))
    try:
        result = await session.execute(product)
        return result.scalars().first()
    except:
        return False

