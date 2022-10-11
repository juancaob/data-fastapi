"""create posts table

Revision ID: 124541f43f86
Revises: 
Create Date: 2022-10-10 17:59:00.345286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "124541f43f86"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
