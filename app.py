from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/stores")
def get_stores():
    return {"stores": stores}


@app.post("/stores")
def create_store():
    req_data = request.get_json()
    new_store = {"name": req_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.get("/stores/<string:name>")
def get_items(name):
    for store in stores:
        if name == store["name"]:
            return {"items": store["items"]}

    return {"message": "No store found with that name"}, 404


@app.post("/stores/<string:name>/items")
def create_item(name):
    req_data = request.get_json()

    for store in stores:
        if name == store["name"]:
            new_item = {"name": req_data["name"], "price": req_data["price"]}
            store["items"].append(new_item)
            return new_item, 201

    return {"message": "No store found with that name"}, 404


@app.get("/stores/<string:name>/items/<string:item_name>")
def get_specific_item(name, item_name):
    for store in stores:
        if name == store["name"]:
            for item in store["items"]:
                if item_name == item["name"]:
                    return {"item": item}

            return {"message": "No item found in the store with that name"}, 404

    return {"message": "No store found with that name"}, 404
