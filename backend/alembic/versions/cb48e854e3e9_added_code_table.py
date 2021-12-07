"""added code table

Revision ID: cb48e854e3e9
Revises: 8db96ca8bd38
Create Date: 2021-12-07 11:17:29.926735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb48e854e3e9'
down_revision = '8db96ca8bd38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'code',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('unique_code', sa.String(), nullable=False),
        sa.Column('is_expired', sa.Boolean(), nullable=False),
        sa.Column('is_verified', sa.Boolean(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('unique_code')
    )
    op.create_index(op.f('ix_code_user_id'), 'code', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_code_user_id'), table_name='code')
    op.drop_table('code')
    # ### end Alembic commands ###
