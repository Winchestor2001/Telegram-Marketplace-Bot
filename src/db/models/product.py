from sqlalchemy import ForeignKey

from . import Base, BaseMixin, List, Mapped, mapped_column, relationship, TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category


class Product(Base, BaseMixin):
    name: Mapped[str]
    image: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    views: Mapped[int] = mapped_column(default=0, nullable=True)
    is_buy: Mapped[bool] = mapped_column(default=False, nullable=True)
    lat: Mapped[float] = mapped_column(nullable=True)
    long: Mapped[float] = mapped_column(nullable=True)

    category_uuid: Mapped[str] = mapped_column(ForeignKey('categorys.uuid'))
    category: Mapped["Category"] = relationship(back_populates="products")

    images: Mapped[List["ProductImage"]] = relationship(back_populates="product")


class ProductImage(Base, BaseMixin):
    image: Mapped[str]
    product_uuid: Mapped[str] = mapped_column(ForeignKey('products.uuid'))
    product: Mapped["Product"] = relationship(back_populates="images")
