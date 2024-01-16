import os
from celery import Celery
import config


cfg = config.config_picker(os.environ['FLASK_ENV'])
celery = Celery('worker', broker=cfg.CELERY_BACKEND, backend=cfg.CELERY_BACKEND)


@celery.task
def test_async(num1, num2):
    results = {'environment': str(os.environ['FLASK_ENV']),
               'redis_url': str(cfg.CELERY_BACKEND),
               'what is 1+1?': num1 + num2,
               'redis_ok?': True,
               'celery_ok?': True,
               'goose_ok?': 'HONK'}
    return results
