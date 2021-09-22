"""Initial migration.

Revision ID: 1fe01ef4c3d9
Revises: 4006c2e998c3
Create Date: 2021-09-22 11:39:43.844830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fe01ef4c3d9'
down_revision = '4006c2e998c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('password', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('username', name='user_username_key')
    )
    # ### end Alembic commands ###
