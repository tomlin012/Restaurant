from typing import List

import pydantic


class InsertOrderRequest(pydantic.BaseModel):
    class Item(pydantic.BaseModel):
        id: int
        prepare_time: int

    items: pydantic.conlist(Item, min_items=1)



class DeleteOrderRequest(pydantic.BaseModel):
    order_ids: pydantic.conlist(int, min_items=1)


class GetOrderResponse(pydantic.BaseModel):
    id: int
    table_id: int
    item_id: int
    prepare_time: int