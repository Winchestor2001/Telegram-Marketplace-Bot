from . import Base, BaseMixin, List, Mapped, mapped_column, relationship, TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product


class Category(Base, BaseMixin):
    name: Mapped[str]
    products: Mapped[List["Product"]] = relationship("Product", back_populates="category")
