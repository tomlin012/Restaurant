from ast import stmt
import datetime
import http

from typing import List
import fastapi
import sqlalchemy as sa

from src import database, utils
from src.features.order import models, schemas


router = fastapi.APIRouter(
    prefix="/orders",
    tags=["order"],
    default_response_class=fastapi.responses.JSONResponse,
)

@router.get(
    "/tables",
    response_model=List[int],
)
def get_tables():
    stmt = sa.select(models.Table.id)
    with database.session() as session:
        return session.execute(stmt).scalars().all()


@router.get(
    "/items",
    response_model=List[int],
)
def get_items():
    stmt = sa.select(models.Item.id)
    with database.session() as session:
        return session.execute(stmt).scalars().all()


@router.get(
    "/table/{table_id}",
    response_model=List[schemas.GetOrderResponse],
)
def get_order_by_table_id(table_id: int):
    stmt = (
        sa.select(models.Order).
        where(models.Order.table_id == table_id)
    )
    with database.session() as session:
        return session.execute(stmt).scalars().all()


@router.post(
    "/table/{table_id}",
    status_code=http.HTTPStatus.NO_CONTENT,
)
def insert_order(
    table_id: int,
    payload: schemas.InsertOrderRequest,
):
    current_time = utils.utcnow()
    get_item_duration_stmt = (
        sa.select(models.Item).
        where(models.Item.id.in_(payload.item_ids))
    )
    with database.session(expire_on_commit=False) as session:
        items = session.execute(get_item_duration_stmt).scalars().all()
        if len(items) < len(payload.item_ids):
            raise fastapi.HTTPException(
                http.HTTPStatus.UNPROCESSABLE_ENTITY,
                detail="item id not found",
            )
        session.bulk_insert_mappings(
            models.Order,
            tuple(
                {
                    "table_id": table_id,
                    "item_id": item.id,
                    "ended_at": current_time + datetime.timedelta(
                        seconds = item.duration
                    ),
                }
                for item in items
            ),
        )
        session.commit()
    return

@router.delete(
    "/table/{table_id}",
    status_code=http.HTTPStatus.NO_CONTENT,
)
def delete_order(
    table_id: int,
    payload: schemas.DeleteOrderRequest,
):
    stmt = (
        sa.delete(models.Order).
        where(
            models.Order.table_id == table_id,
            models.Order.id.in_(payload.order_ids),
        )
    )

    with database.session() as session:
        if session.execute(stmt).rowcount != len(payload.order_ids):
            raise fastapi.HTTPException(
                http.HTTPStatus.UNPROCESSABLE_ENTITY,
                detail="order not found",
            )
        session.commit()