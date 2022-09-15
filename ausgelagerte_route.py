from flask import request

def init_app(app):
    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"
