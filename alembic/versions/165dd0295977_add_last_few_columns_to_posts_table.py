"""add last few columns to posts table

Revision ID: 165dd0295977
Revises: 6bba1ccea712
Create Date: 2022-10-10 19:12:44.178380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "165dd0295977"
down_revision = "6bba1ccea712"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
