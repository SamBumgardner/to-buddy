import yaml

def load_config():
    with open('resources/config.yml') as confFile:
        config = yaml.safe_load(confFile)
    return config

CONFIG = load_config()