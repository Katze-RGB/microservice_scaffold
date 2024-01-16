#you'll need a .env file with a key and stuff I think too, it's in gitignore, get secret key from there

from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

def config_picker(env):
    match str(env):
        case 'development':
            return DevConfig()
        case 'local':
            return LocalConfig()
        case 'production':
            return ProdConfig()


class Config(object):

    @property
    def CELERY_BACKEND(self):
        return str(self.CELERY)

    @property
    def DASHBOARD_URL(self):
        return(self.DASHBOARD_URL)


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    CELERY = 'placeholder_redis_url'
    DASHBOARD_URL = 'placeholder_flower_dashboard_url'


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DASHBOARD_URL = 'placeholder_flower_dashboard_url'

class LocalConfig(Config):
    CELERY = 'redis://redis:6379/0'
    DEBUG = True
    TESTING = True
    DASHBOARD_URL= 'http://localhost:5557'