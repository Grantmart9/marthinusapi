from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/humidity/real')
def HumidityRealTime():
   return {"Humidity":55}

@app.route('/temperature/real')
def TemperatureRealTime():
   return {"Temperature":23}

@app.route('/humidity/history')
def HumidityHistory():
   return [{"Date":"2022-05-20","Humidity":80},{"Date":"2022-05-21","Humidity":90}]

@app.route('/temperature/history')
def TemperatureHistory():
   return [{"Date":"2022-05-20","Temperature":34},{"Date":"2022-05-21","Temperature":23}]

if __name__ == '__main__':
   app.run()