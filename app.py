from datetime import datetime
from flask import Flask
app = Flask(__name__)

# Temperature Sensor real-time value
@app.route("/temperature/realtime", methods=['GET'])
def TemperatureReal():
    return "This is temperature real-time"

# Humidity Sensor real-time value
@app.route("/humidity/realtime", methods=['GET'])
def HumidityReal():
    return "This is humidity real-time"
# Temperature Sensor historical value
@app.route("/temperature/realtime", methods=['GET'])
def TemperatureHistory():
    return "This is temperature History"

# Humidity Sensor historical value
@app.route("/humidity/realtime", methods=['GET'])
def HumidityHistory():
    return "This is humidity History"

if __name__ == '__main__':
   app.run()