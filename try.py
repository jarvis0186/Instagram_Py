import configparser
import json

config = configparser.ConfigParser()
try:
    config.read(".\\config.ini")
    config_default = config["DEFAULT"]
    js_string = json.loads(config_default["js_string"])
    print(js_string["a"])
except:
    print( "Error reading the config file. Please check if the Environment variable ENV_MODE is set" )