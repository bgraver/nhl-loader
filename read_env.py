from configparser import ConfigParser

def read_env():
    config = ConfigParser()
    config.read('env.ini')
    return config
