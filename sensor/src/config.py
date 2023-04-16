import os
from dotenv import load_dotenv

load_dotenv()

SENSOR_DIR = os.getenv('SENSOR_DIR')

load_dotenv(override=True)
