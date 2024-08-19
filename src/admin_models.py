import logging

from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.db import Profile, Product, Category, ProductImage
from markupsafe import Markup
from settings import settings

logger = logging.getLogger("fastapi_app")


class ProfileAdmin(ModelView, model=Profile):
    column_list = [Profile.uuid, Profile.username, Profile.telegram_id]
    column_searchable_list = [Profile.username, Profile.telegram_id]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.uuid, Product.name, Product.category]
    column_searchable_list = [Product.name, Product.uuid]
    column_export_list = [Product.uuid, Product.name, Product.category, Product.images]


class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.uuid, ProductImage.image, ProductImage.product]
    column_searchable_list = [ProductImage.uuid]

    column_formatters = {
        'image': lambda model, field: Markup(
            f'<a href="{model.image}" target="_blank">'
            f'<img src="{model.image}" style="height:50px;" />'
            f'</a>'
        )
    }
    column_formatters_detail = {
        'image': lambda model, field: Markup(
            f'<a href="{model.image}" target="_blank">'
            f'<img src="{model.image}" style="height:150px;" />'
            f'</a>'
        )
    }


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.uuid, Category.name, Category.obj_state]
    column_searchable_list = [Category.name, Category.uuid]


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        if username in settings.admin.usernames and password in settings.admin.passwords:
            # Validate username/password credentials
            # And update session
            request.session.update({"token": "..."})

            return True
        return False

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True
