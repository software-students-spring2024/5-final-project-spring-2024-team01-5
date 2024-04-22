import os

from flask import Flask, render_template
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    CORS(app) # Enable CORS for all routes
    if test_config is not None:
        app.config.update(test_config)

    @app.route('/')
    def home():
        """
        Route for the home page.
        """
        return 'GPA Calculator APP'

    return app