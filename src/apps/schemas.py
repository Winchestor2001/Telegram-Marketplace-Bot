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
    products: List["Product"]


class CreateCategory(BaseModel):
    name: str


class SingleCategory(BaseSchema):
    name: str


class Product(BaseSchema):
    name: str
    image: str
    description: str
    category: SingleCategory


class CreateProduct(BaseModel):
    name: str
    image: str
    description: str
    category_uuid: str
