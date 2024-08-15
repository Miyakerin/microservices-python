"""new fileds for recipe table and create ingredient table

Revision ID: 8a9559f88338
Revises: f04a438c36b4
Create Date: 2024-08-15 14:11:12.548286

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from src.recipes.entities import recipe_entity
from src.recipes.entities import ingredient_entity

# revision identifiers, used by Alembic.
revision: str = "8a9559f88338"
down_revision: Union[str, None] = "f04a438c36b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        ingredient_entity.table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
    )

    op.add_column(
        recipe_entity.table_name,
        sa.Column("user_id", sa.Integer(), nullable=False, default=0),
    )
    op.add_column(
        recipe_entity.table_name, sa.Column("calories", sa.Integer(), nullable=True)
    )
    op.add_column(
        recipe_entity.table_name,
        sa.Column("spice_level", sa.Integer(), nullable=True, default=0),
    )
    op.add_column(
        recipe_entity.table_name,
        sa.Column("is_deleted", sa.Boolean(), nullable=False, default=False),
    )


def downgrade() -> None:
    pass
