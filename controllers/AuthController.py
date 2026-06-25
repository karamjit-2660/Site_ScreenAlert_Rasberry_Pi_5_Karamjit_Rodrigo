import sys
import bcrypt
sys.path.append("../dao")
sys.path.append("../utils")
from flask import Blueprint, request, jsonify
from UserDAO import UserDAO
from Utils import gerar_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"error": "Email e password obrigatórios"}), 400

    dao = UserDAO()
    user = dao.getUserByEmail(email)

    if not user:
        return jsonify({"error": "Utilizador não encontrado"}), 404

    if not bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        return jsonify({"error": "Password incorreta"}), 401

    if user["status"] == "Blocked":
        return jsonify({"error": "Conta bloqueada"}), 403

    if not user["is_verified"]:
        return jsonify({"error": "Conta não verificada"}), 403

    token = gerar_token(user["id"])

    return jsonify({
        "token": token,
        "id": user["id"],
        "name": user["name_user"]
    }), 200