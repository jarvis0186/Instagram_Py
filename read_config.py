import configparser

class config_ini:

    def read_config(self):
        config = configparser.ConfigParser()
        try:
            config.read(".\\Config\\config-AM.ini")
            config_default = config["DEFAULT"]
            print( "Reading config successful")
            return config_default
        except:
            print( "Error reading the config file. Please check if the Environment variable ENV_MODE is set" )