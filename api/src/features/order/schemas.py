import datetime
import pydantic


class InsertOrderRequest(pydantic.BaseModel):
    item_id: int
    prepare_time: int


class DeleteOrderRequest(pydantic.BaseModel):
    order_ids: pydantic.conlist(int, min_items=1)


class GetOrderResponse(pydantic.BaseModel):
    id: int
    table_id: int
    item_id: int
    prepare_time: int

    class Config:
        orm_mode = True