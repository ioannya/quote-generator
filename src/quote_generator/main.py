from typing import Optional

from .db import init_db
from .quote_service import get_random_quote, create_quote, get_categories
from .models import Quote


def display_quote(quote: Optional[Quote]) -> None:
    if quote:
        print("\n" + "="*50)
        print(quote)
        print("="*50 + "\n")
    else:
        print("\nЦитат не найдено.\n")


def main():
    init_db()

    while True:
        print("*** Генератор случайных цитат ***")
        print("1. Получить случайную цитату")
        print("2. Получить случайную цитату по категории")
        print("3. Показать все категории")
        print("4. Добавить новую цитату")
        print("0. Выйти")

        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            quote = get_random_quote()
            display_quote(quote)

        elif choice == "2":
            category = input("Введите категорию: ").strip()
            quote = get_random_quote(category=category)
            display_quote(quote)

        elif choice == "3":
            categories = get_categories()
            if categories:
                print("\nДоступные категории:")
                for cat in categories:
                    print(f"  - {cat}")
            else:
                print("\nКатегорий пока нет.")
            print()

        elif choice == "4":
            text = input("Введите текст цитаты: ").strip()
            category = input("Введите категорию цитаты: ").strip()
            if text and category:
                create_quote(text, category)
                print("Цитата успешно добавлена!\n")
            else:
                print("Текст и категория не могут быть пустыми.\n")

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неизвестный пункт меню. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
