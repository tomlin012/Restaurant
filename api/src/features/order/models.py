import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from src.database.models import TableNameMixin


Base = sa.orm.declarative_base()


class Table(Base, TableNameMixin):
    id = sa.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)


class Item(Base, TableNameMixin):
    id = sa.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    duration = sa.Column(mysql.INTEGER(10, unsigned=True), nullable=False)


class Order(Base, TableNameMixin):
    id = sa.Column(mysql.INTEGER(10, unsigned=True), primary_key=True, autoincrement=True)
    table_id=sa.Column(mysql.INTEGER(10, unsigned=True), sa.ForeignKey("table.id"), nullable=False)
    item_id=sa.Column(mysql.INTEGER(10, unsigned=True), sa.ForeignKey("item.id"), nullable=False)
    ended_at=sa.Column(sa.DateTime, nullable=False, server_default=sa.text("CURRENT_TIMESTAMP"))

    __table_args__ = (
        sa.Index("table_id_item_id", "table_id", "item_id"),
    )