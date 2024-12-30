from flask import Flask, request

app = Flask(__name__)

Stores = [
    {
        'name' : 'MyStore',
        'items' : [
        {
            'name' : 'chair',
            'price' : 200
        },
        {
            'name' : 'Mug',
            'price' : 100
        }
        ]
    },
    {
        'name' : 'Cheda',
        'items' : [
        {
            'name' : 'Books',
            'price' : 100
        },
        {
            'name' : 'Pen',
            'price' : 50
        }
        ]
    }
]


# @app.get('/stores')
@app.route('/stores', methods = ['GET'])
def get_stores():
    return {'stores' : Stores}

@app.route('/stores', methods = ['POST'])
def create_store():
    data = request.get_json()
    new_store = {'name' : data['name'], 'items' : []}
    Stores.append(new_store)
    return new_store, 201

@app.route('/stores/<string:name>/item', methods = ['POST'])
def add_item(name):
    data = request.get_json()
    for store in Stores:
        if store['name'] == name:
            store['items'].append({'name' : data['name'], 'price' : data['price']})
            return "Item added Sucessfully", 201
    return {'message': 'Store not found'}, 404

@app.route('/stores/<string:name>', methods = ["GET"])
def get_store(name):
    for store in Stores:
        if store['name'] == name:
            return store, 200
    return {'message': 'Store not found'}, 404


@app.route('/stores/<string:name>/items', methods = ["GET"])
def get_store_items(name):
    for store in Stores:
        if store['name'] == name:
            return {'items' : store['items']}, 200
    return {'message': 'Store not found'}, 404