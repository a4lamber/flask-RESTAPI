from flask import Flask,request
from db import items,stores
import uuid

app = Flask(__name__)


# end point
@app.route('/')
def index_page():
    return "Hello Docker xiaomi haha!"

#####################################################
# GET


# a single GET end points at /store
@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
    """
    get all the stores information
    Returns:
        _type_: _description_
    """
    return {"stores": list(stores.values())}

@app.get("/item") 
def get_all_items():
    return {"items": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    """
    get a specific store infomation
    Args:
        name (string): name of the store

    Returns:
        _type_: _description_
    """
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404



@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404


#####################################################
# Post

@app.post("/store")
def create_store():
    # get json from client
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    # standard for merge dict
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    
    return store, 201


@app.post("/item")
def create_item():
    # grab the inc json
    item_data = request.get_json()
    
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"},404
    
    item_id = uuid.uuid4().hex
    item = {**item_data,"id":item_id}
    items[item_id] = item
    return item,201

        
