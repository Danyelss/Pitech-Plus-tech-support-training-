#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, request
from google.cloud import datastore
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm

app = Flask(__name__)

@app.route('/pdf/users', methods=['GET'])
def get_users():
    tempPdf = Canvas("users.pdf")
    datastore_client = datastore.Client()
    kind = "TaskUser"
    query = datastore_client.query(kind=kind)
    times = list(query.fetch())
    users = list()
    for time in times:
        tempPdf.setFont("Times-Roman",16)
        #tempPdf.setFillColor(blue)
        tempPdf.drawString(1 * inch, 10 * inch,str(time.key.id)+ " " + str(time["name"]) + " " + str(time["email"]))
    tempPdf.save()

    return "0"

@app.route('/user/add', methods=['POST'])
def create_user():
    # Instantiates a client
    datastore_client = datastore.Client()

    if not request.json or 'name' not in request.json:
        abort(400)

    user_id = request.json["id"]
    item_name = request.json['name']
    email = request.json['email']

    # The kind for the new entity
    kind = "TaskUser"

    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, user_id)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task["email"]=email
    task["name"]=item_name

    # Saves the entity
    datastore_client.put(task)

    return make_response(jsonify({'Status': 'Created'}), 200)

@app.route('/user/<iduser>', methods=['GET'])
def get_user_by_id(iduser):
    datastore_client = datastore.Client()
    kind = "TaskUser"
    user_key = datastore_client.key(kind,iduser)
    user = datastore_client.get(user_key)
    if user:
        return jsonify(user)
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/user/<iduser>', methods=['PUT'])
def update_user_by_id(iduser):

    if not request.json or 'name' not in request.json:
        abort(400)

    item_name = request.json['name']
    email = request.json['email']

    datastore_client = datastore.Client()
    kind = "TaskUser"

    user_key = datastore_client.key(kind,iduser)
    user = datastore_client.get(user_key)

    if user:
        return make_response(jsonify({'error': 'Not found'}), 404) 

    user["email"]=email
    user["name"]=item_name

    datastore_client.put(user)

    return make_response(jsonify({'Status': 'UPDATED'}), 200)


@app.route('/user/<iduser>', methods=['DELETE'])
def delete_user_by_id(iduser):

    if not request.json or 'name' not in request.json:
        abort(400)

    datastore_client = datastore.Client()
    kind = "TaskUser"

    user_key = datastore_client.key(kind,iduser)

    if user_key:
        return make_response(jsonify({'error': 'Not found'}), 404) 

    datastore_client.delete(user_key)

    return make_response(jsonify({'Status': 'DELETED'}), 200)



if __name__ == '__main__':
    app.run(debug=True)