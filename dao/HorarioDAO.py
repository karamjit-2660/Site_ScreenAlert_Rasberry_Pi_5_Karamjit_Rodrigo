import sys
sys.path.append("../config")
from Database import get_connection

class HorarioDAO:
    def getHorarioByUser(self, id_user):
        conn = get_connection()
        if not conn:
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT sm.id, sm.name_medication, sm.description_medication,
                       d.day_of_doce, d.doce
                FROM schedule_medications sm
                JOIN day_for_medications d ON d.id_schedule_medication = sm.id
                WHERE sm.id_user = %s
                ORDER BY sm.name_medication, d.day_of_doce
            """, (id_user,))
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
            conn.close()