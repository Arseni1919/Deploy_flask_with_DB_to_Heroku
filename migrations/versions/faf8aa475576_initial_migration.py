"""Initial migration.

Revision ID: faf8aa475576
Revises: 
Create Date: 2021-09-22 11:32:42.953633

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'faf8aa475576'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    op.drop_table('stations')
    op.add_column('user', sa.Column('name', sa.String(length=128), nullable=True))
    op.drop_constraint('user_username_key', 'user', type_='unique')
    op.drop_column('user', 'password')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password', sa.TEXT(), autoincrement=False, nullable=True))
    op.create_unique_constraint('user_username_key', 'user', ['username'])
    op.drop_column('user', 'name')
    op.create_table('stations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('lat', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('lng', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='stations_pkey')
    )
    op.create_table('feedback',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('comments', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='feedback_pkey'),
    sa.UniqueConstraint('customer', name='feedback_customer_key')
    )
    # ### end Alembic commands ###
