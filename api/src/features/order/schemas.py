import datetime
import pydantic


class InsertOrderRequest(pydantic.BaseModel):
    item_ids: pydantic.conlist(int, min_items=1)


class DeleteOrderRequest(pydantic.BaseModel):
    order_ids: pydantic.conlist(int, min_items=1)


class GetOrderResponse(pydantic.BaseModel):
    id: int
    table_id: int
    item_id: int
    ended_at: datetime.datetime

    class Config:
        orm_mode = True