from typing import Optional

from .models import Quote
from . import repositories
from .mapper import entity_to_domain


def normalize_category(category: str) -> str:
    return category.strip().lower()


def create_quote(text: str, category: str) -> Quote:
    text = text.strip()
    category = normalize_category(category)

    if not text:
        raise ValueError("Текст цитаты не должен быть пустым.")
    if not category:
        raise ValueError("Категория не должна быть пустой.")

    entity = repositories.add_quote(text, category)
    return entity_to_domain(entity)


def get_random_quote(category: Optional[str] = None) -> Optional[Quote]:
    if category is not None:
        category = normalize_category(category)

    entity = repositories.fetch_random_quote(category)
    if entity is None:
        return None

    return entity_to_domain(entity)


def get_categories() -> list[str]:
    return repositories.list_categories()
