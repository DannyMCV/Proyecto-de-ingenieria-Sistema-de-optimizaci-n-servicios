# app/routes/consumo.py
from flask import Blueprint, jsonify

consumo_bp = Blueprint("consumo", __name__)

@consumo_bp.route("/api/consumo", methods=["GET"])
def obtener_consumo():
    # Por ahora retorna datos de prueba
    # Aquí luego conectarás con SQLite
    return jsonify({"mensaje": "Endpoint de consumo funcionando", "data": []})