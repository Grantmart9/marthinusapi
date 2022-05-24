import pyodbc
from datetime import datetime
from flask import Flask

cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:homeautomation2.database.windows.net,1433;Database=homeautomation3;Uid=Grant;Pwd={Xiobh@nmart9};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

cursor = cnxn.cursor()

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
# User Authentication
@app.route("/Users", methods=['GET'])
def Users():
    return {
        "Identification": {
            "Name": "Grant",
            "LastName": "Marthinus",
            "email": "grantmarthinus@gmail.com",
            "cell": "+27 72 528 1424",
            "Token": "#nsjd2@1nndn",
            "Autherized": True
        }
    }


if __name__ == '__main__':
    app.run()
