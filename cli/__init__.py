# -- coding: utf-8 --
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S')

CLOUD_HOST = 'https://api-mcc.ainngpu.io'
# CLOUD_HOST = 'http://localhost:8070'
