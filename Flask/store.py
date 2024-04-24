from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "my store",
        "items": [
            {
                "name": "chair",
                "price": 20
            }
        ]
    }
]

@app.route("/store", methods=["GET"])
def get_store():
    return {'store': stores}

@app.route('/store', methods=["POST"])
def create_store():
    request_data = request.get_json()
    if 'name' not in request_data:
        return {'error': 'Name is required'}, 400  # Bad Request
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


if __name__ == '__main__':
    app.run(debug=True)
