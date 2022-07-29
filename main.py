from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Medium"
    
@app.route("/doos")
def doos():
    return "doos"


if __name__ == '__main__':
    app.run(port=5000)