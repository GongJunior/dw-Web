"""empty message

Revision ID: 4e9f18e4d48b
Revises: 
Create Date: 2020-06-02 14:06:15.408380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e9f18e4d48b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('names',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roll', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=120), nullable=False),
    sa.Column('listname_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['listname_id'], ['names.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('words')
    op.drop_table('names')
    # ### end Alembic commands ###
