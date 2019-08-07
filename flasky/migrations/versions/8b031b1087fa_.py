"""empty message

Revision ID: 8b031b1087fa
Revises: 38c4e85512a9
Create Date: 2019-08-01 18:08:54.291673

"""

# revision identifiers, used by Alembic.
revision = '8b031b1087fa'
down_revision = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###