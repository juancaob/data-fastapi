"""add content column to posts table

Revision ID: d9e93a5bf1d5
Revises: 124541f43f86
Create Date: 2022-10-10 18:33:00.929610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d9e93a5bf1d5"
down_revision = "124541f43f86"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
