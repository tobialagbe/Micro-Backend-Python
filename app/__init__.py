import os

from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple test endpoint
    @app.route('/test')
    def hello():
        return 'working!'

    from . import auth
    app.register_blueprint(auth.bp)

    return app
