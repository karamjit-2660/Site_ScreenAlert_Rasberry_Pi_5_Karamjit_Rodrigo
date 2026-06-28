import sys
sys.path.append("../config")
from Database import get_connection

class MensagensDAO:
    def getMensagensByUser(self, id_user):
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, text_message, DATE_FORMAT(sent_at, '%d/%m/%Y %H:%i') as sent_at
                FROM messages 
                WHERE id_user = %s 
                ORDER BY sent_at DESC
                LIMIT 1
            """, (id_user,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

def historicoMensagens(self, id_user):
    conn = get_connection()
    if not conn:
        return None

    try:
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT
                id,
                text_message,
                DATE_FORMAT(sent_at, '%d/%m/%Y %H:%i:%s') AS sent_at
            FROM messages
            WHERE id_user = %s
            ORDER BY sent_at DESC
        """

        cursor.execute(query, (id_user,))
        return cursor.fetchall()

    except Exception as e:
        print(e)
        return None

    finally:
        cursor.close()
        conn.close()