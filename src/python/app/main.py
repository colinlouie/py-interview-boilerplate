import uuid
from typing import Annotated, Union

from fastapi import FastAPI, HTTPException, Query
from interview.question import Question
from interview.models.item import Item

app = FastAPI()


@app.get("/")
async def welcome():
    q = Question()
    return {"data": q.foo()}


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^(?:hello|world)$")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    # simulate feature flag
    if q == "hello":
        results.update({"q": "different_execution_path"})
    # validation
    elif q:
        results.update({"q": q})
    return results


# # Path based parameters
# # e.g. /items/1
# @app.get("/items/{item_id}")
# async def read_items(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# POST creates an item given data in the request body
@app.post("/items/")
async def create_item(item: Item):
    return item


# Query-string based parameters
# e.g. /query_param?item_id=1
@app.get("/query_param")
async def query_param(item_id: int):
    return item_id


# PUT using a Model with Field (spec including example values)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
