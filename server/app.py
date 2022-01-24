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
handler = logging.FileHandler('./logs/temp.log')  # datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.log'
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# initialize database
db.init_app(app)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>', 200


if __name__ == '__main__':
    logger.info('Start back-end at http://localhost:5000/...')
    app.run(host='localhost', port=5000)
