from . import Base, BaseMixin, Mapped, mapped_column, BigInteger


class Profile(Base, BaseMixin):
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=True)
