import configparser
import os

def get_config_value(key):
    config = configparser.ConfigParser()
    file_path = "configuration.properties"
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found")
        raise FileNotFoundError(f"Configuration file {file_path} does not exist")
    
    config.read(file_path)
    return config.get("DEFAULT", key)

def get_api_url():
    return get_config_value("API_URL")
