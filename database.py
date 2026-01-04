import sqlite3
import mysql.connector


class BrowserDB:
    """Manages secure hybrid storage (MariaDB Cloud + SQLite Local)."""

    def __init__(self):
        self.cloud_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '', #Your database password
            'database': 'nexus_browser'
        }
        self.local_path = "nexus_local.db"
        self._init_local_db()

    def _init_local_db(self):
        with sqlite3.connect(self.local_path) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS local_history 
                         (title TEXT, url TEXT, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

    def login_user(self, username, password):
        conn = None
        try:
            conn = mysql.connector.connect(**self.cloud_config)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, username FROM users WHERE username=%s AND password=%s", (username, password))
            return cursor.fetchone()
        except Exception as e:
            print(f"Login error: {e}")
            return None
        finally:
            if conn: conn.close()

    def register_user(self, username, password):
        conn = None
        try:
            conn = mysql.connector.connect(**self.cloud_config, autocommit=True)
            cursor = conn.cursor()
            # Security check: Check if exists
            cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
            if cursor.fetchone(): return False

            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            return True
        except Exception as e:
            print(f"Reg error: {e}")
            return False
        finally:
            if conn: conn.close()

    def save_data(self, user_id, title, url, table="history"):
        if not user_id: return
        conn = None
        try:
            conn = mysql.connector.connect(**self.cloud_config, autocommit=True)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {table} (user_id, title, url) VALUES (%s, %s, %s)",
                           (user_id, title, url))
        except:
            pass
        finally:
            if conn: conn.close()

    def get_user_data(self, user_id, table="history"):
        if not user_id: return []
        conn = None
        try:
            conn = mysql.connector.connect(**self.cloud_config)
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT title, url FROM {table} WHERE user_id=%s ORDER BY id DESC LIMIT 100", (user_id,))
            return cursor.fetchall()
        finally:
            if conn: conn.close()
