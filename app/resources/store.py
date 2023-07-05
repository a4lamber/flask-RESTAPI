'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-07-05 12:49:20
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-07-05 12:53:53
 # @ Description:
'''


import uuid
from flask import request
from flask_smorest import abort,Blueprint
from flask.views import MethodView
from db import stores
from schemas import StoreSchema


blp = Blueprint("stores",__name__, description="Operations on stores")

# this conects flask_smorest to this method_view
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found")

    def put(self,store_id):
        store_data = request.get_json()

        if "name" not in store_data:
            abort(
                400,
                message="Bad request. Ensure 'name' are included in the\
                    JSON payload",
            )

        try:
            store = stores[store_id]
            store |= store_data

            return store
        except KeyError:
            abort(404, message="Store not found.")


@blp.route("/store")    
class StoreList(MethodView):
    def get(self):
        return {"stores": list((stores.values()))}

    @blp.arguments(StoreSchema)
    def post(self,store_data):
        store_data = request.get_json()
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists.")
        
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        
        return store
            