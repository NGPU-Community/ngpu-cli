# -- coding: utf-8 --
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG,
#                     # format: 指定输出的格式和内容，format可以输出很多有用信息
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S')

CLOUD_HOST = 'http://121.40.165.67:8070'
