"""rename age to years_old

Revision ID: c267dc0ee15b
Revises: 156d38bec788
Create Date: 2026-02-14 14:43:01.801310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c267dc0ee15b'
down_revision = '156d38bec788'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'age', new_column_name='years_old')

    # ### end Alembic commands ###


def downgrade():
    op.alter_column('users', 'years_old', new_column_name='age')

    # ### end Alembic commands ###
