import sys
sys.path.append("../dao")
sys.path.append("../utils")
from flask import Blueprint, jsonify, request
from MensagensDAO import MensagensDAO
from Utils import verificar_token

mensagens_bp = Blueprint("mensagens", __name__)

@mensagens_bp.route("/mensagens", methods=["GET"])
def getMensagens():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = verificar_token(token)

    if not payload:
        return jsonify({"error": "Token inválido"}), 401

    id_user = payload["id"]

    dao = MensagensDAO()
    mensagem = dao.getMensagensByUser(id_user)

    if not mensagem:
        return jsonify({"error": "Sem mensagens"}), 404

    return jsonify(mensagem), 200