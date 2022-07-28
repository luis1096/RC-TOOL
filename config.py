from distutils.debug import DEBUG
from decouple import config

BAUDRATE = config('BAUDRATE', default=115200, cast=int)
DEBUG = config('DEBUG', default=True, cast=bool)
DRIVER = config('DRIVER', default='/dev/ttyACM', cast=str)
HOST = config('HOST', default='0.0.0.0', cast=str)
PORT = config('PORT', default=5000, cast=int)