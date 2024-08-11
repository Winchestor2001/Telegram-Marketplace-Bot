from typing import List
from datetime import datetime

from pydantic import BaseModel


class BaseSchema(BaseModel):
    uuid: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Category(BaseSchema):
    name: str
    products: List["SingleProduct"] | None = []

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

    class Config:
        from_attributes = True


class Product(BaseSchema):
    name: str
    image: str
    description: str
    category: SingleCategory

    class Config:
        from_attributes = True


class CreateProduct(BaseModel):
    name: str
    image: str
    description: str
    category_uuid: str

    class Config:
        from_attributes = True
