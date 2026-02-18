# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración básica
    app.config["SECRET_KEY"] = "clave-secreta-temporal"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///consumo.db"

    # Registrar blueprints (rutas)
    from app.routes.consumo import consumo_bp
    app.register_blueprint(consumo_bp)

    return app