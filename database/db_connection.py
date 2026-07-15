"""
db_connection.py
----------------
Author  : Dnyaneshwari  Sonawane
College : DYPCOEI, SPPU, Pune
GitHub  : https://github.com/dnyaneshwari2309

Handles MySQL connection using environment variables so
credentials are never hardcoded in source files.
"""

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host":     os.getenv("DB_HOST", "localhost"),
    "user":     os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "hospital_db"),
}


def get_connection():
    """Return a live MySQL connection, or None on failure."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"[DB ERROR] Could not connect to MySQL: {e}")
    return None
