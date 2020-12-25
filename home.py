import flask
from flask import request, jsonify,render_template

app= flask.Flask(__name__)

@app.route('/api/home/turnonlights', methods=['GET'])
def headLightsOn():

    return "Head Lights turned on!!!!"


app.run(host="0.0.0.0",port=9999)