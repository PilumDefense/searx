#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/searx/")

#from searx import app as application
import searx
from searx.webapp import app  as application
application.secret_key = 'Add your secret key'

