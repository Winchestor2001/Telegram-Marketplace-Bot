from sqlalchemy import ForeignKey

from . import Base, BaseMixin, List, Mapped, mapped_column, relationship, TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category


class Product(Base, BaseMixin):
    name: Mapped[str]
    image: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    category_uuid: Mapped[str] = mapped_column(ForeignKey('categorys.uuid'))
    category: Mapped["Category"] = relationship(back_populates="products")
