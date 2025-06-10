from flask import Flask, request
from db import items, stores
import uuid

app = Flask(__name__)

# @app.get('/stores')
@app.route('/stores', methods = ['GET'])
def get_stores():
    return {'stores': list(stores.values())}, 200

@app.route('/stores', methods = ['POST'])
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    stores[store_id] = {**(store_data), 'id' : store_id}
    return "Store created successfully", 201

@app.route('/item', methods = ['POST'])
def add_item():
    item_data = request.get_json()
    item_id = uuid.uuid4().hex
    items[item_id] = {**(item_data), "id" : item_id}
    return "Item created successfully", 201

@app.route('/items', methods = ['GET'])
def get_items():
    return {'items': list(items.values())}, 200

@app.route('/stores/<string:store_id>', methods = ["GET"])
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {'message': 'Store not found'}, 404

@app.route('/items/<string:item_id>', methods = ["GET"])
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {'message': 'Store not found'}, 404