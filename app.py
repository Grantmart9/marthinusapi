from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/humidity/real')
def humidity():
   return {"Humidity":55}

@app.route('/temperature/real')
def temperature():
   return {"Temperature":23}

if __name__ == '__main__':
   app.run()