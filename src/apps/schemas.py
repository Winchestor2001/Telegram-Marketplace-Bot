from typing import List
from datetime import datetime
import logging

from pydantic import BaseModel, Field, root_validator, validator


logger = logging.getLogger(__name__)


class BaseSchema(BaseModel):
    uuid: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Category(BaseSchema):
    name: str

    class Config:
        from_attributes = True


class CreateCategory(BaseModel):
    name: str

    class Config:
        from_attributes = True


class SingleCategory(BaseSchema):
    name: str

    class Config:
        from_attributes = True


class SingleProduct(BaseSchema):
    name: str
    image: str
    description: str
    price: float

    class Config:
        from_attributes = True


class ProductImages(BaseModel):
    image: str

    class Config:
        from_attributes = True


class Product(BaseSchema):
    name: str
    description: str
    views: int
    is_buy: bool
    price: float
    lat: float
    long: float
    category: SingleCategory
    images: List[ProductImages]

    class Config:
        from_attributes = True


class CreateProduct(BaseModel):
    telegram_id: int
    name: str
    description: str
    price: float
    lat: float
    long: float
    category_uuid: str
    images: List[str] = None

    class Config:
        from_attributes = True


class FilterProduct(BaseModel):
    name: str | None = None
    category_uuid: str | None = None

