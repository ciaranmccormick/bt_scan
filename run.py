import json
import logging
import sys
from logging.config import dictConfig
from stretch_blt_scan import mqtt
from stretch_blt_scan.scan import perform_scan
from time import sleep
logger = logging.getLogger(__name__)


try:
    from settings import MQTT, LOGGING_CONF, PARTICIPANT
except ImportError as er:
    logger.error(er)
    sys.exit(0)

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
MSG_BUF_SIZE = 600  # message buffer size

dictConfig(LOGGING_CONF)


logger.debug("starting up...")

while True:
    logger.debug("Performing scan.")
    devices = perform_scan()
    logger.debug("Scan finished.")
    logger.debug(devices)

    for d in devices:
        logger.debug("".format(d))

    logger.debug("Sleeping for 30 seconds.")
    sleep(30)

