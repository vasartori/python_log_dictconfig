import logging
import logging.config
import json

with open('teste_log/config.json', 'r')as json_config:
    config = json.loads(json_config.read())
logging.config.dictConfig(config)
