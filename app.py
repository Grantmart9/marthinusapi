from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_cors import CORS

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
CORS(app)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

###################################################################################################################
##############                These endpoints are protected  ######################################################
###################################################################################################################

##############                   Room Temperature & Humidity  #####################################################
###################################################################################################################
@app.route('/room')
@jwt_required()
def room():
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
##############                   Room Temperature & Humidity  #####################################################
###################################################################################################################
@app.route('/dashboard')
@jwt_required()
def dashboard():
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

##############                   Irrigation           #############################################################
###################################################################################################################
@app.route('/irrigation')
@jwt_required()
def irrigation():
    return ({
        "current_flow": "2",
        "soil_humidity":"33",
        "accumulated_flow_today":"334",
        "total_water_day": [],
        "out_door_temperature": "22",
        "out_door_humidity": "85",
        "irrigation_start_times":[],
        "Date": "2022-05-27 18:50:12:342"
        })

##############                   Fertigation           ############################################################
###################################################################################################################
@app.route('/fertigation')
@jwt_required()
def fertigation():
    return ({
        "Mix1Setpoint": "2.2",
        "Mix2Setpoint":"3.3",
        "Mix3Setpoint":"5.4",
        "Mix4Setpoint":"6.1",
        "Mix5Setpoint":"6.4",
        "Mix6Setpoint":"3.0",
        "pH_Setpoint":"4.5",
        })

##############                   Energy          ##################################################################
###################################################################################################################
@app.route('/energy')
@jwt_required()
def energy():
    return ({
        "inverter_power_output": "12",
        "battery_time_left":"30",
        "batter_percentage":"99.78",
        "inverter_solar_charge":"300",
        "inverter_charge_history":[],
        })

##############                   Weather          #################################################################
###################################################################################################################
@app.route('/weather')
@jwt_required()
def weather():
    return ({
        "Icon": "13",
        "IconPhrase": "Mostly cloudy w/ showers",
        "HasPrecipitation": "true",
        "PrecipitationType": "Rain",
        "PrecipitationIntensity": "Light",
        "ShortPhrase": "Variable clouds with a shower",
        "LongPhrase": "Variable clouds with a shower in the area",
        "PrecipitationProbability": "44",
        "ThunderstormProbability": "9",
        "RainProbability": "44",
        "Wind": {
          "Speed": {
            "Value": "11.1",
            "Unit": "km/h",
            "UnitType": "7"
          },
          "Direction": {
            "Degrees": "219",
            "Localized": "SW",
            "English": "SW"
          }
        },
        "WindGust": {
          "Speed": {
            "Value": "29.6",
            "Unit": "km/h",
            "UnitType": "7"
          },
          "Direction": {
            "Degrees": "242",
            "Localized": "WSW",
            "English": "WSW"
          }
        },
        "Rain": {
          "Value": "0.6",
          "Unit": "mm",
          "UnitType": "3"
        },
        "Evapotranspiration": {
          "Value": "0.2",
          "Unit": "mm",
          "UnitType": "3"
        },
        "SolarIrradiance": {
          "Value": "514.2",
          "Unit": "W/m²",
          "UnitType": "33"
        }
      })

if __name__ == '__main__':
    app.run()