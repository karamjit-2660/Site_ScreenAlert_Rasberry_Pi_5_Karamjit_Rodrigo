import sys
sys.path.append("../controllers")
sys.path.append("../dao")
sys.path.append("../utils")
sys.path.append("../config")

from flask import Flask
from flask_cors import CORS

from AuthController import auth_bp
from MensagensController import mensagens_bp
from HistoricoController import historico_bp
from HorarioController import horario_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(mensagens_bp)
app.register_blueprint(historico_bp)
app.register_blueprint(horario_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)