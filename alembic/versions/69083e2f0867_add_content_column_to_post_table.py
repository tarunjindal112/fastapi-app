"""add content column to post table

Revision ID: 69083e2f0867
Revises: 55158548be77
Create Date: 2024-05-21 10:59:32.362015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69083e2f0867'
down_revision: Union[str, None] = '55158548be77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
