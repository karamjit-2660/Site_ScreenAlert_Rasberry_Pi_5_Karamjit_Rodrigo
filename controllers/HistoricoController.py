import sys
sys.path.append("../dao")
sys.path.append("../utils")
from flask import Blueprint, jsonify, request
from MensagensDAO import MensagensDAO
from Utils import verificar_token

historico_bp = Blueprint("historico", __name__)

@historico_bp.route("/historicoMensagens", methods=["GET"])
def historicoMensagens():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = verificar_token(token)

    if not payload:
        return jsonify({"error": "Token inválido"}), 401

    dao = MensagensDAO()
    historico = dao.historicoMensagens(payload["id"])

    if historico is None:
        return jsonify({"error": "Erro ao obter histórico"}), 500

    return jsonify(historico), 200