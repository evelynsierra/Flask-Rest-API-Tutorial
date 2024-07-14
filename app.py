from flask import Flask, request

app = Flask(__name__) # creating flask app

stores = [
    {
        "name" : "My Store",
        "items" : [
            {
                "name": "Chair",
                "price" : "15.99"
            }
        ]
    }
]

@app.get("/store") # localhost:5000/store
def get_stores(): # this is an API endpoint or Flask route
    return {"stores":stores}

@app.post("/store")
def create_store():
    # Get JSON to convert to dictionary in Python
    request_data = request.get_json() 
    new_store = {"name" : request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201 # 201 means okay and create a new data

@app.post("/store/<string:name>/item") # if client wants a custom name hitting the API
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {"name" : request_data["name"], "price" : request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message" : "Store Not Found"}, 404

@app.get('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message" : "Store Not Found"}, 404

@app.get('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message" : "Store Not Found"}, 404

if __name__ == "__main__":
    app.run(debug=True)