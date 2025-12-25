from typing import Optional
from .db import get_connection
from .entities import QuoteEntity


def add_quote(text: str, category: str) -> QuoteEntity:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "insert into quotes (text, category) values (?, ?)",
            (text, category),
        )
        conn.commit()
        quote_id = cursor.lastrowid
        return QuoteEntity(id=quote_id, text=text, category=category)
    finally:
        conn.close()


def fetch_random_quote(category: Optional[str] = None) -> Optional[QuoteEntity]:
    conn = get_connection()
    try:
        cursor = conn.cursor()

        if category:
            cursor.execute(
                """
                select id, text, category
                from quotes
                where category = ?
                order by random()
                limit 1;
                """,
                (category,),
            )
        else:
            cursor.execute(
                """
                select id, text, category
                from quotes
                order by random()
                limit 1;
                """
            )

        row = cursor.fetchone()
        if row is None:
            return None

        return QuoteEntity(id=row[0], text=row[1], category=row[2])
    finally:
        conn.close()


def list_categories() -> list[str]:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "select distinct category from quotes order by category;"
        )
        return [row[0] for row in cursor.fetchall()]
    finally:
        conn.close()
