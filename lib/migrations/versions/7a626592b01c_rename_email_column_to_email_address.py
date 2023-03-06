"""Rename email column to email_address

Revision ID: 7a626592b01c
Revises: 791279dd0760
Create Date: 2023-03-06 16:37:32.144033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a626592b01c'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='email_address')


def downgrade() -> None:
    op.alter_column('students', 'email_address', new_column_name='email')
