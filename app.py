import pyodbc
from datetime import datetime
from flask import Flask

server = 'tcp:homeautomation2.database.windows.net' 
database = 'homeautomation3' 
username = 'Grant' 
password = 'Xiobh@nmart9' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

app = Flask(__name__)
# Sensor 1
@app.route("/Sensor1", methods=['GET'])
def Sensor1():
    cursor.execute("SELECT * FROM Humidity")
    row = cursor.fetchmany()
    print(row);
    cursor.execute("SELECT * FROM Temperature")
    row = cursor.fetchmany()
    print(row);
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

# User Authentication
@app.route("/Users", methods=['GET'])
def Users():
    cursor.execute("SELECT * FROM Users")
    row = cursor.fetchmany()
    print(row);
    return {
        "Identification": {
            "Name": "Grant",
            "LastName": "Marthinus",
            "email": "grantmarthinus@gmail.com",
            "cell": "+27 72 528 1424",
            "Token": "#nsjd2@1nndn",
            "Autherized": "1"
        }
    }
if __name__ == '__main__':
    app.run()
