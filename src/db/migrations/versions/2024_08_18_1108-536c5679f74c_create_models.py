"""create models

Revision ID: 536c5679f74c
Revises: dcf203363eb2
Create Date: 2024-08-18 11:08:56.215413

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "536c5679f74c"
down_revision: Union[str, None] = "dcf203363eb2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        op.f("uq_profiles_telegram_id"), "profiles", ["telegram_id"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("uq_profiles_telegram_id"), "profiles", type_="unique"
    )
    # ### end Alembic commands ###
