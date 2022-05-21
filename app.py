from datetime import datetime
from flask import Flask
app = Flask(__name__)

# Temperature Sensor real-time value
@app.route("/Sensor1", methods=['GET'])
def TemperatureReal():
    return {"RealTime":{"DateTime":"2022-05-10","Temperature":23,"Humidity":76},"Historical":[{"DateTime":"2022-05-10","Temperature":23,"Humidity":76},{"DateTime":"2022-05-10","Temperature":23,"Humidity":76}]}



if __name__ == '__main__':
   app.run()