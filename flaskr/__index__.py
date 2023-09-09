import os
from flask import Flask, render_template

def create_app(text_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, flaskr.sqlite)
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/images')
    def images():
        return render_template('images.html')

    @app.route('/todo')
    def todo():
        return render_template('todo.html')

    return app