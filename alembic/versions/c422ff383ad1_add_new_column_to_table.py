"""Add new column to table

Revision ID: c422ff383ad1
Revises: 
Create Date: 2023-10-29 20:47:23.884762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c422ff383ad1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the new column
    # op.add_column('addressbook', sa.Column('location', sa.Integer))

    op.drop_column('addressbook','location')

    


def downgrade():
    #Revert the column addition
    op.drop_column('addressbook', sa.Column('location', sa.Integer(), nullable=True))

    