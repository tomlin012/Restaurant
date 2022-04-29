"""insert items and tables

Revision ID: 95a009579e31
Revises: 775b272a1d9b
Create Date: 2022-04-29 10:25:14.837448

"""
from alembic import op
import sqlalchemy as sa

from src.features.order import models

# revision identifiers, used by Alembic.
revision = '95a009579e31'
down_revision = '775b272a1d9b'
branch_labels = None
depends_on = None


def upgrade():
    tables = [{} for _ in range(5)]
    items = [{} for _ in range(5)]
    session = sa.orm.Session(bind=op.get_bind())
    session.bulk_insert_mappings(models.Table, tables)
    session.bulk_insert_mappings(models.Item, items)
    session.commit()


def downgrade():
    session = sa.orm.Session(bind=op.get_bind())
    session.execute(sa.delete(models.Table))
    session.execute(sa.delete(models.Item))
    session.commit()
