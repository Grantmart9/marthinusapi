from datetime import datetime
from flask import Flask
app = Flask(__name__)
import pyodbc

server = 'homeautomation2.database.windows.net'
database = 'homeautomation3'
username = 'Grant'
password = 'Xiobh@nmart9'
driver= '{ODBC Driver 17 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

@app.route('/humidity/real')
def HumidityRealTime():
   return {"Humidity":55}

@app.route('/temperature/real')
def TemperatureRealTime():
   return {"Temperature":23}

@app.route('/humidity/history')
def HumidityHistory():
   return {"Humidity":23,"Humidity":24}

@app.route('/temperature/history')
def TemperatureHistory():
   return {"Temperature":23,"Temperature":24}

if __name__ == '__main__':
   app.run()