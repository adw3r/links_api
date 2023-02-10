import configparser
import os
import pathlib

from dotenv import load_dotenv

PACKAGE_FOLDER = pathlib.Path(__file__).parent
config = configparser.ConfigParser()
config.read(pathlib.Path(PACKAGE_FOLDER, 'config.ini'))
load_dotenv()
config_general = config['general']

URL = os.environ['URL']
DOMAINS = ('ezc.info', 'izp.info', 'zfh.info')
ZENNO_KEY = os.environ['ZENNO_KEY']
DEBUG = os.environ.get('DEBUG', False)
config_general['DEBUG'] = DEBUG
DEBUG = config_general.getboolean('DEBUG')
REFERRALS_API_HOST: str = config_general.get('REFERRALS_API_HOST')
REFERRALS_API_PORT: int = config_general.getint('REFERRALS_API_PORT')

if not DEBUG:
    HOST = config_general.get('HOST', '0.0.0.0')
    PORT = config_general.getint('PORT', 8184)
else:
    HOST = config_general.get('TEST_HOST', 'localhost')
    PORT = config_general.getint('TEST_PORT', 8284)
