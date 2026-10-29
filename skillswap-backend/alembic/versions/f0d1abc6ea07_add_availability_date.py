"""add availability date

Revision ID: f0d1abc6ea07
Revises: 1d1f4b60cd25
Create Date: 2026-10-03 03:15:53.699359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0d1abc6ea07'
down_revision: Union[str, Sequence[str], None] = '1d1f4b60cd25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "availabilityslot",
        sa.Column("availability_date", sa.Date(), nullable=True),
    )

    op.execute(
        """
        UPDATE availabilityslot
        SET availability_date = DATE '2026-10-03'
        WHERE availability_date IS NULL
        """
    )

    op.alter_column(
        "availabilityslot",
        "availability_date",
        existing_type=sa.Date(),
        nullable=False,
    )

    op.create_index(
        "ix_availabilityslot_availability_date",
        "availabilityslot",
        ["availability_date"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_availabilityslot_availability_date",
        table_name="availabilityslot",
    )
    op.drop_column("availabilityslot", "availability_date")
