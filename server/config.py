import json


class Config:
    def __init__(self, json_file: str):
        with open(json_file, mode='r') as f:
            obj = f.read()
        obj = json.loads(obj)
        try:
            self.DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(
                username=obj['username'],
                password=obj['password'],
                host=obj['host'],
                port=obj['port'],
                db=obj['database'])
            self.SQLALCHEMY_DATABASE_URI = self.DB_URI
            self.SQLALCHEMY_TRACK_MODIFICATIONS = False
            self.SQLALCHEMY_ECHO = False
        except KeyError:
            print('Database configuration missing key')
