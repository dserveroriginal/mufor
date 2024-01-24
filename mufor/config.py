import json

def load():
    """Load configuration."""
    file=open(".personal/config.json","r")
    return json.load(file)