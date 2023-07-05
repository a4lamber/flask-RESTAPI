"""
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-04-25 09:28:14
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-04-26 10:46:06
 # @ Description:
 """

# from flask import Flask, request
# from flask_smorest import abort
# from db import items, stores
# import uuid

from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(StoreBlueprint)
api.register_blueprint(ItemBlueprint)



# @app.route("/")
# def index_page():
#     return "Dockerize!"


# #####################################################
# # GET
# #####################################################


# # a single GET end points at /store
# @app.get("/store")  # http://127.0.0.1:5000/store
# def get_all_stores():
#     """
#     get all the stores information

#     :return _type_: _description_
#     """
#     return {"stores": list(stores.values())}


# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     """
#     get a specific store information
#     Args:
#         name (string): name of the store

#     Returns:
#         _type_: _description_
#     """
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="Store not found")


# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="item not found")


# #####################################################
# # Post
# # - create store
# # - create item
# #####################################################


# @app.post("/store")
# def create_store():
#     """
#     Handle client json payload to create a store, assign unique identifier
#     and write it to pseudo-database.
#     -------------------------------------------------
#     Example:
#     Step 1: client pass in a json payload like the following,
#     {
#         "name": "My Store"
#     }
#     Step2: Create a unique identify (hash) and merge it
#     to the payload
#     {
#         "name": "My Store",
#         "id": "9a39bddfc5444639aede1eab78547ec0"
#     }
#     Step3: write it to the database, new database for store looks like
#     {
#         "stores": [
#                 {
#                         "id": "9a39bddfc5444639aede1eab78547ec0",
#                         "name": "My Store"
#                 }
#         ]
#     }
#     Error handling:
#     1. Check whether the payload has key "name" in it
#     2. Check whether the store name is duplicated
#     -------------------------------------------------
#     Returns:
#         dict, code: store, status code 201
#     """
#     # get json from client
#     store_data = request.get_json()

#     # error handling: check "name"
#     if "name" not in store_data:
#         abort(400, message="Bad request. Ensure name is included in the Json payload")

#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message="Store already exists.")

#     # create a unique identifier and merge with client's json
#     # and write it to database
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store

#     return store, 201


# @app.post("/item")
# def create_item():
#     """
#     Handle client json payload to create a new item, assign unique identifier
#     for the payload and write it to pseudo-database.
#     Example:
#     Step 1: client pass in a json payload like the following,
#     {
#         "name": "Chair",
#         "price": 17.99,
#         "store_id": "add6e49bc20248e59eb2a8ebb38a813f"
#     }
#     Step 2: Create a unique identify (hash) and merge it
#     to the payload
#     {
#         "id": "45b5abd1cd2d4b168dd59302145fdec6",
#         "name": "Chair",
#         "price": 17.99,
#         "store_id": "65771d36f7ab4dfbbf3975d8914e7bf5"
#     }
#     Step 3: add it to items database
#     {
#         "items": [
#                 {
#                         "id": "45b5abd1cd2d4b168dd59302145fdec6",
#                         "name": "Chair",
#                         "price": 17.99,
#                         "store_id": "65771d36f7ab4dfbbf3975d8914e7bf5"
#                 }
#         ]
#     }
#     Error handling:
#     1. Check whether the payload has key "name","store_id" and "price"
#     2. Check no duplicate item within store
#     3. Check if the store exists
#     Returns:
#         _type_: 201, successfully update
#     """
#     # grab the inc json
#     item_data = request.get_json()

#     # handling bad requests
#     if (
#         "price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad request. Ensure 'price', 'store_id', and\
#                 'name' are included in the JSON payload.",
#         )

#     # handling repeating item within store
#     for item in items.values():
#         if (
#             item_data["name"] == item["name"]
#             and item_data["store_id"] == item["store_id"]
#         ):
#             abort(400, message="item already exists")

#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found")

#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item
#     return item, 201


# #####################################################
# # Delete
# #####################################################

# @app.delete("/item/<string:item_id>/")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted."}
#     except KeyError:
#         abort(404, message="Item not found")


# @app.delete("/store/<string:store_id>/")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted."}
#     except KeyError:
#         abort(404, message="Store not found")


# #####################################################
# # Put
# #####################################################

# @app.put("/item/<string:item_id>/")
# def update_item(item_id):
#     item_data = request.get_json()

#     if "price" not in item_data or "name" not in item_data:
#         abort(
#             400,
#             message="Bad request. Ensure 'price', and 'name' are\
#                   included in the JSON payload",
#         )

#     try:
#         item = items[item_id]
#         item |= item_data

#         return item
#     except KeyError:
#         abort(404, message="Item not found.")


# @app.put("/store/<string:store_id>/")
# def update_store(store_id):
#     store_data = request.get_json()

#     if "name" not in store_data:
#         abort(
#             400,
#             message="Bad request. Ensure 'name' are included in the\
#                   JSON payload",
#         )

#     try:
#         store = stores[store_id]
#         store |= store_data

#         return store
#     except KeyError:
#         abort(404, message="Store not found.")