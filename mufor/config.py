import json
import os

def load():
    """Load configuration."""
    
    if not os.path.exists(".files/config.json"):
        file=open("config/default_config.json","r")
    else:
        file=open(".files/config.json","r")
    config=json.load(file)
    file.close()
    
    config["path"]["links"]=config["path"]["links"]%{"here":os.getcwd()}
    
    return config
