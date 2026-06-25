import sys
sys.path.append("../config")
from Database import get_connection

class UserDAO:
    def getUserByEmail(self, email):
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE email = %s AND deleted_at IS NULL AND is_verified = 1 AND id_cuidador IS NOT NULL", (email,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()