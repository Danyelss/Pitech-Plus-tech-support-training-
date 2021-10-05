#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, request
from google.cloud import datastore
app = Flask(__name__)

@app.route('/api/list', methods=['GET'])
def get_task():
    datastore_client = datastore.Client()
    kind = "Task"
    query = datastore_client.query(kind=kind)
    times = list(query.fetch())
    users = list()
    for time in times:
        user_as_dict = dict()
        user_as_dict["name"] = time.key.name
        user_as_dict["price"] = time["price"]
        users.append(user_as_dict)
    return jsonify(users)

@app.route('/api/add', methods=['POST'])
def create_task():
    # Instantiates a client
    datastore_client = datastore.Client()

    if not request.json or 'name' not in request.json:
        abort(400)

    item_name = request.json['name']
    price = request.json['price']

    # The kind for the new entity
    kind = "Task"

    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, item_name)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task["price"]=price

    # Saves the entity
    datastore_client.put(task)

    return "0"

if __name__ == '__main__':
    app.run(debug=True)