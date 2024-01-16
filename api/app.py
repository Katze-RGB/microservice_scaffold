import os
from flask import Flask, jsonify, redirect
from config import config_picker
from celery_app import test_async
from healthcheck import HealthCheck


app = Flask(__name__)
config = config_picker(os.environ['FLASK_ENV'])
app.config.from_object(config)
health = HealthCheck()


def worker_available():
    test_async.apply_async(args=(1, 1))
    return True, "Worker Ok"


def self_available():
    return True, "Flask Ok"


health.add_check(worker_available)
health.add_check(self_available)
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())


@app.route('/healthcheck_verbose')
def celery_available():
    task = test_async.apply_async(args=(1, 1))
    return jsonify(output=task.get())


@app.route('/dashboard', methods=['GET'])
def dash_redirect():
    return redirect(app.config['DASHBOARD_URL'])


if __name__ == '__main__':
        from waitress import serve
        serve(app, host="0.0.0.0", port=5000)

