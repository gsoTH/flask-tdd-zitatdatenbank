from multiprocessing.dummy import connection
from flask import Flask
from flask import request
from flask import g as globaleVariablen
import sqlite3
from ausgelagerte_route import init_app


def create_app():
    app = Flask(__name__)

    init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
