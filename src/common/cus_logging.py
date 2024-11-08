import logging
import logging.config
import yaml
import os

DEFAULT_LOGGING_CONFIG = """version: 1

formatters:
  console:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    formatter: console
    stream: ext://sys.stdout

root:
  level: INFO
  handlers: [ console ]"""


def _setup_logger():
  if os.path.isfile("log_conf.yaml"):
    with open('log_conf.yaml', 'r') as file:
      config = yaml.load(file, Loader=yaml.FullLoader)
      file.close()
  else:
    with open('log_conf.yaml', 'w') as file:
      file.write(DEFAULT_LOGGING_CONFIG)
      file.close()
      config = yaml.safe_load(DEFAULT_LOGGING_CONFIG)

  logging.config.dictConfig(config)

  return logging.getLogger(os.getenv('SERVICE_NAME', __name__))


logger = _setup_logger()
