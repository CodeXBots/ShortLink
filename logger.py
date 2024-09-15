import logging
import logging.config
import sys

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
