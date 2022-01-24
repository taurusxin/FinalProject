from flask import Flask
import logging
import datetime

from database import db

from config import Config

# main application object
app = Flask(__name__)
# flask application configuration
config = Config('config.json')
app.config.from_object(config)

# add custom logger handler
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('./logs/temp.log')
# datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.log'
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# initialize database
logger.info('initializing database')
db.init_app(app)
logger.info('database initialized')


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>', 200
