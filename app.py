import pyodbc
from datetime import datetime
from flask import Flask

cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:homeautomation2.database.windows.net,1433;Database=homeautomation3;Uid=Grant;Pwd={Xiobh@nmart9};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

cursor = cnxn.cursor()

app = Flask(__name__)


if __name__ == '__main__':
    app.run()
