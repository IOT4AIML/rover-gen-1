import flask
from flask import request, jsonify,render_template
from servicecomponents.roverservices  import  CoreServices 

app= flask.Flask(__name__)

@app.route('/api/home/lightson', methods=['GET'])
def headLightsOn():
     light=CoreServices()
     return light.headLightsOn(True)
@app.route('/api/home/lightoff', methods=['GET'])
def headLightsOn():
     light=CoreServices()
     return light.headLightsOn()


app.run(host="0.0.0.0",port=9999)