"""empty message

Revision ID: bdca4b5f35f7
Revises: dbf9e9f2b93c
Create Date: 2018-02-28 02:44:52.295252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdca4b5f35f7'
down_revision = 'dbf9e9f2b93c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
