##import pyodbc
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

##server = 'homeautomation2.database.windows.net'
##database = 'homeautomation3'
##username = 'Grant'
##password = 'Xiobh@nmart9'
##driver= '{ODBC Driver 17 for SQL Server}'

##cnxn = pyodbc.connect('Server=tcp:homeautomation2.database.windows.net,1433;Initial Catalog=homeautomation3;Persist Security Info=False;User ID=Grant;Password=Xiobh@nmart9;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;')
##cursor = cnxn.cursor()


@app.route('/humidity/real')
def HumidityRealTime():
    return {"Humidity": 55}


@app.route('/temperature/real')
def TemperatureRealTime():
    return {"Temperature": 23}


@app.route('/humidity/history')
def HumidityHistory():
    return [{"Temperature": 23}, {"Temperature": 24}]


@app.route('/temperature/history')
def TemperatureHistory():
    return [{"Temperature": 23}, {"Temperature": 24}]


if __name__ == '__main__':
    app.run()
