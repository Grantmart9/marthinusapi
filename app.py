from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'Grant', 'Xiobh@nmart9'),
    User(2, 'Xio', '9594'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

###################################################################################################################
##############                These endpoints are protected  ######################################################
###################################################################################################################

###########  Room Temperature & Humidity
@app.route('/RoomTemperatureHumidity')
@jwt_required()
def protected():
    return ({
    "room_1": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_2": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_3": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_4": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_5": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_6": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_7": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_8": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_9": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    },
    "room_10": {
        "Temperature": "23",
        "Humidity": "88",
        "O2":"2",
        "TemperatureSetpoint": "22",
        "HumiditySetpoint": "85",
        "Date": "2022-05-27 18:50:12:342"
    }
})

if __name__ == '__main__':
    app.run()