import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "192.168.11.199",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "sa_system"
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Erro ao ligar à BD: {e}")
        return None