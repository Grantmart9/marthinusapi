import pyodbc
from datetime import datetime
from flask import Flask,jsonify

server = 'tcp:homeautomation2.database.windows.net' 
database = 'homeautomation3' 
username = 'Grant' 
password = 'Xiobh@nmart9' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

app = Flask(__name__)
# Sensor 1
@app.route("/Sensor1/Humidity", methods=['GET'])
def Sensor1Humidty():
    cursor.execute("SELECT * FROM Humidity")
    result = cursor.fetchmany(1)

    ## create list ##
    data = []
    ## Loop through cols and historySize ##
    for row in result:
        ## Create dictionary for list ##
        DataDictionary = {"Index": 1,"Date":(row[1]) ,"Humidity":(row[2])}

        ## Append dictionary to list ##
        data.append(DataDictionary)

    ## print data to console ##
    print(DataDictionary)
 
    ## Return list and convert to json ##
    return (jsonify(DataDictionary))

@app.route("/Sensor1/Temperature", methods=['GET'])
def Sensor1Temperature():
    cursor.execute("SELECT * FROM Temperature")
    result = cursor.fetchmany(1)

    ## create list ##
    data = []
    ## Loop through cols and historySize ##
    for row in result:
        ## Create dictionary for list ##
        DataDictionary = {"Index": 1,"Date":(row[1]) ,"Humidity":(row[2])}

        ## Append dictionary to list ##
        data.append(DataDictionary)

    ## print data to console ##
    print(DataDictionary)
 
    ## Return list and convert to json ##
    return (jsonify(DataDictionary))

@app.route("/Users", methods=['GET'])
def Sensor1Users():
    cursor.execute("SELECT * FROM Users")
    result = cursor.fetchmany(1)

    ## create list ##
    data = []
    ## Loop through cols and historySize ##
    for row in result:
        ## Create dictionary for list ##
        DataDictionary = {"Index": 1,"Username":(row[1]) ,"Password":(row[2])}

        ## Append dictionary to list ##
        data.append(DataDictionary)

    ## print data to console ##
    print(DataDictionary)
 
    ## Return list and convert to json ##
    return (jsonify(DataDictionary))
if __name__ == '__main__':
    app.run()
