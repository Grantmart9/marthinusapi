from datetime import datetime
from flask import Flask
app = Flask(__name__)

# Temperature Sensor real-time value
@app.route("/temperature", methods=['GET'])
def get_demo():
    return "This is temperature"

# Humidity Sensor real-time value
@app.route("/humidity", methods=['GET'])
def get_demo():
    return "This is humidity"


if __name__ == '__main__':
   app.run()