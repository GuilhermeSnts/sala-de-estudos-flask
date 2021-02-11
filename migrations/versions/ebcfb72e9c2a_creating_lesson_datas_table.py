"""Creating lesson_data table

Revision ID: ebcfb72e9c2a
Revises: 937619cef753
Create Date: 2020-09-16 22:40:57.126401

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "ebcfb72e9c2a"
down_revision = "937619cef753"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "lesson_data",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("xml_raw_data", sa.Text(), nullable=True),
        sa.Column("json_xml", sa.JSON(), nullable=True),
        sa.Column("raw_index", sa.Text(), nullable=True),
        sa.Column("json_index", sa.JSON(), nullable=True),
        sa.Column("raw_sync", sa.Text(), nullable=True),
        sa.Column("json_sync", sa.JSON(), nullable=True),
        sa.Column("lesson_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["lesson_id"],
            ["lessons.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("lesson_data")
    # ### end Alembic commands ###
