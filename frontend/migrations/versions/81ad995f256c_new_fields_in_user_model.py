"""new fields in user model

Revision ID: 81ad995f256c
Revises: 4183fe833d30
Create Date: 2018-03-09 14:38:26.286405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81ad995f256c'
down_revision = '4183fe833d30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
