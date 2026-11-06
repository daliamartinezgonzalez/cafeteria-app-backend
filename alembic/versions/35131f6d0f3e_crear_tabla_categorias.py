"""crear tabla categorias

Revision ID: 35131f6d0f3e
Revises: 2a1f70881449
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '35131f6d0f3e'
down_revision: Union[str, Sequence[str], None] = '2a1f70881449'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categorias',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre_categoria', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('nombre_categoria')
    )


def downgrade() -> None:
    op.drop_table('categorias')