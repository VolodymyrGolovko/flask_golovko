"""commit

Revision ID: bca50fc31a8d
Revises: 8ebea352b025
Create Date: 2025-01-25 23:18:07.905111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bca50fc31a8d'
down_revision = '8ebea352b025'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('is_active')
        batch_op.drop_column('category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###
