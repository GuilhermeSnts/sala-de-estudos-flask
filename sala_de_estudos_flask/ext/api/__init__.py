from flask import Flask

from sala_de_estudos_flask.ext.api.routes import bp


def init_app(app: Flask):
    app.register_blueprint(bp)
