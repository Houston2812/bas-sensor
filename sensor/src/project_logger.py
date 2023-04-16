import os
import logging, sys
from config import SENSOR_DIR

logger = logging.getLogger('sensor_logger')

c_handler = logging.StreamHandler(sys.stdout)
c_handler.setLevel(logging.DEBUG)

if os.path.exists(f'{SENSOR_DIR}/logs') == False:
    os.mkdir(f'{SENSOR_DIR}/logs')

with open(f'{SENSOR_DIR}/logs/sensor.logs', 'w') as f:
    pass

f_handler = logging.FileHandler(f'{SENSOR_DIR}/logs/sensor.logs')
f_handler.setLevel(logging.WARNING)

c_format = logging.Formatter("%(name)s - %(pathname)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(pathname)s - %(name)s - %(levelname)s - %(message)s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logging.basicConfig(level=logging.DEBUG, handlers=[logging.NullHandler()])