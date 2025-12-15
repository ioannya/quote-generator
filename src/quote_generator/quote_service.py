import random
import sqlite3
from typing import Optional

from .db import get_connection
from .models import Quote


def insert_quote(text: str, category: str) -> None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO quotes (text, category) VALUES (?, ?)",
            (text, category)
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении цитаты: {e}")
        raise
    finally:
        conn.close()


def get_random_quote(category: Optional[str] = None) -> Optional[Quote]:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        if category:
            cursor.execute(
                "SELECT id, text, category FROM quotes WHERE category = ?;",
                (category,)
            )
        else:
            cursor.execute("SELECT id, text, category FROM quotes;")

        rows = cursor.fetchall()
        if not rows:
            return None

        row = random.choice(rows)
        return Quote(id=row[0], text=row[1], category=row[2])
    except sqlite3.Error as e:
        print(f"Ошибка при получении цитаты: {e}")
        return None
    finally:
        conn.close()


def get_categories() -> list[str]:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT category FROM quotes ORDER BY category;")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    except sqlite3.Error as e:
        print(f"Ошибка при получении категорий: {e}")
        return []
    finally:
        conn.close()
