#__init__.py
from flask import Flask
from app.utils import mysql_util
import logging
from datetime import datetime

app = Flask(__name__, static_folder="static")
# the secret key shouldn't be hardcoded
app.secret_key = "1f5ed6af44756bd1395d80dfc8861c4b45b7eba8a85d07afcf89d9c581d850e9"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# configure logging to show DEBUG messages
app.logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

# log to a file for debugging
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

# ensure the database is set up
mysql_util.ensure_database()

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%B %d, %Y at %I:%M %p'):
    return datetime.strptime(str(value), '%Y-%m-%d %H:%M:%S').strftime(format)

from app import routes
