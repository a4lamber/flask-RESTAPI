'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-07-05 14:47:50
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-07-05 14:54:02
 # @ Description:
 '''

from marshmallow import Schema, fields, validate

class ItemSchema(Schema):
    # dump_only: only for serialization (data to json)
    id = fields.Str(dump_only=True)
    # It must be in the json payload
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)
    
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    
    
    
