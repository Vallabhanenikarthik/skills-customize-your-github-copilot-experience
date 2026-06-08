from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class ItemCreate(BaseModel):
    name: str
    description: str = ""


class Item(ItemCreate):
    id: int


_items: List[dict] = []
_next_id = 1


def _find_item(item_id: int):
    for it in _items:
        if it["id"] == item_id:
            return it
    return None


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    it = _find_item(item_id)
    if not it:
        raise HTTPException(status_code=404, detail="Item not found")
    return it


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global _next_id
    obj = item.dict()
    obj["id"] = _next_id
    _next_id += 1
    _items.append(obj)
    return obj


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    it = _find_item(item_id)
    if not it:
        raise HTTPException(status_code=404, detail="Item not found")
    it.update(item.dict())
    return it


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    it = _find_item(item_id)
    if not it:
        raise HTTPException(status_code=404, detail="Item not found")
    _items.remove(it)
    return None
