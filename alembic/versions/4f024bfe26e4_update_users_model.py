"""Update users model

Revision ID: 4f024bfe26e4
Revises: f331786221c7
Create Date: 2025-04-26 09:52:02.553022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f024bfe26e4'
down_revision: Union[str, None] = 'f331786221c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
