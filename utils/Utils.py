import jwt
import sys
sys.path.append("../config")
from config import JWT_SECRET

def gerar_token(user_id):
    payload = {
        "id": user_id
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

def verificar_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None