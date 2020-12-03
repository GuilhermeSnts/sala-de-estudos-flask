"""lesson_id on lesson_data mus be unique

Revision ID: da830b27bad5
Revises: ebcfb72e9c2a
Create Date: 2020-09-17 00:22:13.159682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da830b27bad5'
down_revision = 'ebcfb72e9c2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'lesson_data', ['lesson_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lesson_data', type_='unique')
    # ### end Alembic commands ###