from flask import Flask, request
import uuid
from db import stores, items

app = Flask(__name__)


@app.get("/stores")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/stores")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {"id": store_id, **store_data}
    stores[store_id] = new_store
    return new_store, 201


@app.get("/items")
def get_items():
    return {"items": list(items.values())}


@app.post("/items")
def create_item():
    item_data = request.get_json()

    if item_data["store_id"] not in stores:
        return {"message": "No store found to add item"}, 404

    item_id = uuid.uuid4().hex
    new_item = {"id": item_id, **item_data}
    items[item_id] = new_item
    return new_item, 201


@app.get("/stores/<string:store_id>/items/<string:item_id>")
def get_specific_item(store_id, item_id):
    if store_id not in stores:
        return {"message": "No store found with that id"}, 404

    if item_id not in items:
        return {"message": "No item found with that id"}, 404

    store_items = []

    for item_key, item_value in items.items():
        if item_key == item_id and item_value["store_id"] == store_id:
            store_items.append(item_value)

    return {"items": store_items}
