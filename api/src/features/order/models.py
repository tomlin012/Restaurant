import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from src.database.models import TableNameMixin


Base = sa.orm.declarative_base()


class Table(Base, TableNameMixin):
    id = sa.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)


class Item(Base, TableNameMixin):
    id = sa.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)


class Order(Base, TableNameMixin):
    id = sa.Column(mysql.INTEGER(10, unsigned=True), primary_key=True, autoincrement=True)
    table_id=sa.Column(mysql.INTEGER(10, unsigned=True), nullable=False)
    item_id=sa.Column(mysql.INTEGER(10, unsigned=True), nullable=False)
    prepare_time=sa.Column(mysql.INTEGER(10, unsigned=True), nullable=False)

    __table_args__ = (
        sa.ForeignKeyConstraint(
            ['table_id'], ['table.id'],
            name='fk_table_id',
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ['item_id'], ['item.id'],
            name='fk_item_id',
            ondelete="CASCADE",
        ),
        sa.Index("ix_table_id", "table_id"),
        sa.Index("ix_item_id", "item_id"),
    )