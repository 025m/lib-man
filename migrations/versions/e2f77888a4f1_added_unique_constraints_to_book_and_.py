"""Added unique constraints to book, and publisher models.

Revision ID: e2f77888a4f1
Revises: 5e1d8ed7badf
Create Date: 2023-11-04 11:40:13.686335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2f77888a4f1'
down_revision = '5e1d8ed7badf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['title'])
        batch_op.create_unique_constraint(None, ['isbn'])

    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
