import flask
from flask import request, jsonify,render_template
from servicecomponents.roverservices  import  CoreServices as cs

app= flask.Flask(__name__)

@app.route('/api/home/turnonlights', methods=['GET'])
def headLightsOn():
     light=cs.CoreServices()
     return light.headLightsOn()


app.run(host="0.0.0.0",port=9999)