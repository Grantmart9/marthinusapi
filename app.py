from datetime import datetime
from flask import Flask
app = Flask(__name__)

# Sensor 1
@app.route("/Sensor1", methods=['GET'])
def Sensor1():
    return {
  "realtime": {
    "dateTime": "2022-05-21",
    "temperature": 23.4,
    "humidity": 76,
    "temperature_set_point": 23.5,
    "humidity_set_point": 76.8
  },
  "historical": [
    {
      "dateTime": "2022-05-21",
      "temperature": 23.4,
      "humidity": 76,
      "temperature_set_point": 23.5,
      "humidity_set_point": 76.8
    },
    {
      "dateTime": "2022-05-21",
      "temperature": 23.4,
      "humidity": 76,
      "temperature_set_point": 23.5,
      "humidity_set_point": 76.8
    },
    {
      "dateTime": "2022-05-21",
      "temperature": 23.4,
      "humidity": 76,
      "temperature_set_point": 23.5,
      "humidity_set_point": 76.8
    }
  ]
}



if __name__ == '__main__':
    app.run()
