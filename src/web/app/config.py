class Config:
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'


class DevConfig(Config):
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'ship-dev'
    USERNAME = 'root'
    PASSWORD = 'mysql'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8"
    DB_URI = DB_URI.format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    MQTT_BROKER_URL = 'localhost'
    MQTT_BROKER_PORT = 1883
    MQTT_USERNAME = "admin"
    MQTT_PASSWORD = "public"
    MQTT_REFRESH_TIME = 1.0

    TD_SERVER_HOST = ''
    TD_CLIENT_USER = ''
    TD_CLIENT_PASSWORD = ''
    TD_SERVER_PORT = 6020
    TD_SERVER_DATABASE = ''

    REDIS_SERVER_HOST = 'localhost'
    REDIS_CLIENT_PASSWORD = ''
    REDIS_SERVER_PORT = 6379
    REDIS_SERVER_DATABASE = ''

    JOBS = [
        {
            'id': 'ship_info_to_db',
            'func': 'app.schedual.dev_test:store_ship_from_cache',
            'args': '',
            'trigger': {
                'type': 'interval',
                'seconds': 60
            }
        }
    ]


class ProdConfig(Config):
    DEBUG = True


config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
