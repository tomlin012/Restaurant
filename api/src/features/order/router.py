import http
from typing import List

import fastapi

from src import database
from src.features.order import schemas


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
    db_conn = database.generate_conn()
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM `table`")
        return tuple(row["id"] for row in cursor.fetchall())


@router.get(
    "/items",
    response_model=List[int],
)
def get_items():
    db_conn = database.generate_conn()
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM `item`")
        return tuple(row["id"] for row in cursor.fetchall())


@router.get(
    "/table/{table_id}",
    response_model=List[schemas.GetOrderResponse],
)
def get_order_by_table_id(table_id: int):
    db_conn = database.generate_conn()
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM `order` WHERE table_id=%s", table_id)
        return tuple(
            {
                "id": row["id"],
                "table_id": row["table_id"],
                "item_id": row["item_id"],
                "prepare_time": row["prepare_time"],
            }
            for row in cursor.fetchall()
        )


@router.get(
    "/item/{item_id}",
    response_model=List[schemas.GetOrderResponse],
)
def get_order_by_table_id(item_id: int):
    db_conn = database.generate_conn()
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM `order` WHERE item_id=%s", item_id)
        return tuple(
            {
                "id": row["id"],
                "table_id": row["table_id"],
                "item_id": row["item_id"],
                "prepare_time": row["prepare_time"],
            }
            for row in cursor.fetchall()
        )


@router.post(
    "/table/{table_id}",
    status_code=http.HTTPStatus.NO_CONTENT,
)
def insert_order(
    table_id: int,
    payload: schemas.InsertOrderRequest,
):
    db_conn = database.generate_conn()
    with db_conn:
        cursor = db_conn.cursor()
        cursor.executemany(
            '''INSERT INTO `order`(table_id, item_id, prepare_time) VALUES(%s, %s, %s)''',
            tuple(
                (table_id, item.id, item.prepare_time)
                for item in payload.items
            )
        )
        db_conn.commit()
    return


@router.delete(
    "/table/{table_id}",
    status_code=http.HTTPStatus.NO_CONTENT,
)
def delete_order(
    table_id: int,
    payload: schemas.DeleteOrderRequest,
):
    stmt = ''' DELETE FROM  `order` WHERE table_id=%s AND id IN (%s) '''%(
        table_id,
        ",".join([str(order_id) for order_id in payload.order_ids]),
    )
    db_conn = database.generate_conn()
    with db_conn:
        cursor = db_conn.cursor()
        cursor.execute(stmt)
        db_conn.commit()
    return