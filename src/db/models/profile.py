from typing import TYPE_CHECKING, List

from sqlalchemy.orm import relationship

from . import Base, BaseMixin, Mapped, mapped_column, BigInteger

if TYPE_CHECKING:
    from .product import Product

class Profile(Base, BaseMixin):
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=True)
    username: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=True)

    products: Mapped[List["Product"]] = relationship("Product", back_populates="profile")

    def __str__(self):
        return self.username
