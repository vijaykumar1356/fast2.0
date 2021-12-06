"""empty message

Revision ID: 8db96ca8bd38
Revises: 
Create Date: 2021-12-03 22:35:28.785253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8db96ca8bd38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('mail', sa.String(), nullable=False),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('uuid', sa.String(), nullable=False),
        sa.Column('profile_pic', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('oauth_verfied', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
