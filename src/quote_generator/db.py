import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "quotes.sqlite3"


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def init_db() -> None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                category TEXT NOT NULL
            );
            """
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_quotes_category ON quotes(category);"
        )
        conn.commit()
        print(f"База данных инициализирована по пути: {DB_PATH}")
    except sqlite3.Error as e:
        print(f"Ошибка при инициализации БД: {e}")
        raise
    finally:
        conn.close()
