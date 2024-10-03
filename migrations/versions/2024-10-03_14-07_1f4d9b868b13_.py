"""empty message

Revision ID: 1f4d9b868b13
Revises: 
Create Date: 2024-10-03 14:07:01.702988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f4d9b868b13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.String(length=36), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('total_amount', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_uuid', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('tax', sa.DECIMAL(precision=5, scale=2), nullable=False),
    sa.Column('discount', sa.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('stock_quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_uuid')
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_item_id', sa.String(length=36), nullable=False),
    sa.Column('order_id', sa.String(length=36), nullable=True),
    sa.Column('product_uuid', sa.String(length=36), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('tax_amount', sa.DECIMAL(precision=5, scale=2), nullable=False),
    sa.Column('discount', sa.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('total_price', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.ForeignKeyConstraint(['product_uuid'], ['products.product_uuid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_item_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('products')
    op.drop_table('orders')
    # ### end Alembic commands ###