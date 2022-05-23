import pyodbc
from datetime import datetime
from flask import Flask
app = Flask(__name__)

connection = pyodbc.connect(
    'Server=tcp:homeautomation2.database.windows.net,1433;Initial Catalog=homeautomation3;Persist Security Info=False;User ID=Grant;Password=Xiobh@nmart9;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;')
# with conn.cursor() as cursor:
##        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
##        row = cursor.fetchone()
# while row:
##            print (str(row[0]) + " " + str(row[1]))
##            row = cursor.fetchone()

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
