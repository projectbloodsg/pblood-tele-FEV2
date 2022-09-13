import sys
import logging
logging.basicConfig(filename='/var/www/JensenHshoots/pblood-tele-FEV2/logging.log', level=logging.INFO) 
sys.path.insert(0, '/var/www/JensenHshoots/pblood-tele-FEV2')
from flaskapp import app as application
