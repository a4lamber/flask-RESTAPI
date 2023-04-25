from flask import Flask,request

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }    
        ]
    }
]



# end point
@app.route('/')
def hello_world():
    return "Hello Docker xiaomi haha!"

# a single GET end points at /store
@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
    """
    get all the stores information
    Returns:
        _type_: _description_
    """
    return {"stores":stores}


@app.post("/store")
def create_store():
    # get json from client
    request_data = request.get_json()
    # add and append
    new_store = {"name": request_data["name"], \
                 "items":[]}
    
    stores.append(new_store)
    
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    """
    add item for a specific stored "name"
    Args:
        name (string): the name of the store

    Returns:
        _type_: _description_
    """
    # grab the inc json
    request_data = request.get_json()
    # find match within store O(N) (better with dict for stores?)
    for store in stores:
        if store["name"] == name:
            # if match, grab, append and return it
            new_item = {"name": request_data["name"],
                        "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
        
    return {"message": "Store not found!"}, 404
        

@app.get("/store/<string:name>")
def get_store(name):
    """
    get a specific store infomation
    Args:
        name (string): name of the store

    Returns:
        _type_: _description_
    """
    for store in stores:
        if store["name"] == name:
            return store
    
    return {"message": "Store not found"}, 404



@app.get("/store/<string:name>/item")
def get_item_in_stores(name):
    """
    get items in a specific store
    Args:
        name (_type_): name of the store

    Returns:
        _type_: _description_
    """
    for store in stores:
        if store["name"] == name:
            # good habit to return as a json (prevent breaking)
            return {"items": store["items"]}
    
    return {"message": "Store not found"}, 404

