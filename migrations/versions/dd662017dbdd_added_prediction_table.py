"""Added Prediction table

Revision ID: dd662017dbdd
Revises: 
Create Date: 2024-12-08 13:41:54.672683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd662017dbdd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prediction', schema=None) as batch_op:
        batch_op.alter_column('company',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=120),
               nullable=False)
        batch_op.alter_column('car_model',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=120),
               nullable=False)
        batch_op.alter_column('year',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('fuel_type',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('driven',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('predicted_price',
               existing_type=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prediction', schema=None) as batch_op:
        batch_op.alter_column('predicted_price',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('driven',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('fuel_type',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('year',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('car_model',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('company',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###
