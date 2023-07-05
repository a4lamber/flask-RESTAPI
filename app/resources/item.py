'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-07-05 12:56:22
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-07-05 12:56:35
 # @ Description:
'''


import uuid
from flask import request
from flask_smorest import abort,Blueprint
from flask.views import MethodView
from db import items
from schemas import ItemSchema,ItemUpdateSchema


blp = Blueprint("items",__name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self,item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")
    
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found")
    
    @blp.arguments(ItemUpdateSchema)
    def put(self,item_data,item_id):
        try:
            item = items[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found.")
                  
@blp.route("/item")    
class ItemList(MethodView):
    def get(self):
        return {"items": list((items.values()))}
    
    @blp.arguments(ItemSchema)
    def post(self, item_data):        
        # handling repeating item within store
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message=f"Item already exists.")


        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item
    
    