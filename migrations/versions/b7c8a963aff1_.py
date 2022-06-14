"""empty message

Revision ID: b7c8a963aff1
Revises: 85fa57044f31
Create Date: 2022-06-08 14:55:13.135965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7c8a963aff1'
down_revision = '85fa57044f31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('words',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=50), nullable=False),
    sa.Column('phonetic', sa.String(length=50), nullable=True),
    sa.Column('mandarin', sa.String(length=150), nullable=True),
    sa.Column('phoneticM', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('word')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('words')
    # ### end Alembic commands ###