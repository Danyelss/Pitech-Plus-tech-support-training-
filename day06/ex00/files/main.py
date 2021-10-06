#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, request
from google.cloud import datastore
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm

app = Flask(__name__)

@app.route('/pdf/users', methods=['GET'])
def get_users():
    tempPdf = Canvas("users.pdf", pagesize=(8.5 * inch, 11 * inch))
    datastore_client = datastore.Client()
    kind = "TaskUser"
    query = datastore_client.query(kind=kind)
    times = list(query.fetch())
    i = 0;
    for time in times:
        tempPdf.setFont("Times-Bold",16)
        tempPdf.setFillColor("blue")
        tempPdf.drawString(100, 11*inch-100-i, str(time["id"])+ " " + str(time.key.name) + " " + str(time["email"]))
        i -= 16
    tempPdf.save()

    try:
        return send_file("users.pdf", attachment_filename='users.pdf')
    except Exception as e:
        return str(e)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)