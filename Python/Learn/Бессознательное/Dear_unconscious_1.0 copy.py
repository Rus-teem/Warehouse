"""Диалог с бессознательным (консольная версия)."""

import random
import time
from typing import Optional


def unconscious_ready() -> bool:
    """Случайным образом определяет готовность бессознательного."""
    return random.choice([True, False])


def unconscious_answer() -> str:
    """Возвращает случайный ответ бессознательного."""
    return random.choice(["Да", "Нет", "Попробуй позже", "Не сейчас", "Ответ скрыт", "Это важно для тебя", "Доверься интуиции"])


def ask_question() -> Optional[str]:
    """Запрашивает вопрос у пользователя. Возвращает None при выходе."""
    print("\nЗадай свой вопрос (или пусто/exit для выхода):")
    q = input("> ").strip()
    if not q or q.lower() in {"exit", "quit", "q"}:
        return None
    return q


def session_loop():
    """Основной цикл диалога с проверкой готовности и ожиданием."""
    print("Диалог с бессознательным (консольная версия)")
    print("Команды: exit / quit / q — выйти.\n")
    while True:
        input("Нажми Enter, чтобы начать попытку... ")
        if unconscious_ready():
            question = ask_question()
            if question is None:
                print("Выход.")
                return
            answer = unconscious_answer()
            print(f"\nОтвет бессознательного: {answer}\n")
        else:
            wait_minutes = random.randint(1, 3)
            wait_seconds = wait_minutes * 3
            print(f"\nБессознательное не готово. Следующая попытка через {wait_minutes} мин.\n")
            time.sleep(wait_seconds)


if __name__ == "__main__":
    try:
        session_loop()
    except KeyboardInterrupt:
        print("\n\nОстановлено пользователем (Ctrl+C).")
