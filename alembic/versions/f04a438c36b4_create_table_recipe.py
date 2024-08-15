"""create table recipe

Revision ID: f04a438c36b4
Revises: 
Create Date: 2024-08-14 22:40:00.545626

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from src.recipes.entities.recipe_entity import table_name

# revision identifiers, used by Alembic.
revision: str = "f04a438c36b4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table(table_name)
