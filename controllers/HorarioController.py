import sys
sys.path.append("../dao")
sys.path.append("../utils")
from flask import Blueprint, jsonify, request
from HorarioDAO import HorarioDAO
from Utils import verificar_token

horario_bp = Blueprint("horario", __name__)

@horario_bp.route("/horario", methods=["GET"])
def getHorario():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = verificar_token(token)

    if not payload:
        return jsonify({"error": "Token inválido"}), 401

    dao = HorarioDAO()
    horario = dao.getHorarioByUser(payload["id"])

    if horario is None:
        return jsonify({"error": "Erro ao obter horário"}), 500

    return jsonify(horario), 200