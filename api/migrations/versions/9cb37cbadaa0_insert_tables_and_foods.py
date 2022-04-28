"""insert tables and items

Revision ID: 9cb37cbadaa0
Revises: 9c8dfcd4d0e4
Create Date: 2022-04-23 20:31:52.851368

"""
from alembic import op
import sqlalchemy as sa

from src.features.order import models

# revision identifiers, used by Alembic.
revision = '9cb37cbadaa0'
down_revision = '9c8dfcd4d0e4'
branch_labels = None
depends_on = None


def upgrade():
    tables = [
        {}
        for _ in range(10)
    ]
    items = [
        {
            "duration": i * 60,
        }
        for i in range(1, 11)
    ]
    session = sa.orm.Session(bind=op.get_bind())
    session.bulk_insert_mappings(models.Table, tables)
    session.bulk_insert_mappings(models.Item, items)
    session.commit()


def downgrade():
    session = sa.orm.Session(bind=op.get_bind())
    session.execute(sa.delete(models.Table))
    session.execute(sa.delete(models.Item))
    session.commit()
