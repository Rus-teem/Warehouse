import random
import time
from typing import Optional

# Функция для генерации готовности бессознательного
def unconscious_ready() -> bool:
    return random.choice([True, False])

# Функция, которая отвечает на вопрос пользователя
def unconscious_answer() -> str:
    return random.choice([
        "Да", "Нет", "Попробуй позже", "Не сейчас",
        "Ответ скрыт", "Это важно для тебя", "Доверься интуиции"
    ])

def ask_question() -> Optional[str]:
    print("\nЗадай свой вопрос (или пусто/exit для выхода):")
    q = input("> ").strip()
    if not q or q.lower() in {"exit", "quit", "q"}:
        return None
    return q

def session_loop():
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
            wait_seconds = wait_minutes * 60
            print(f"\nБессознательное не готово. Следующая попытка через {wait_minutes} мин.\n")
            # Если не хочешь реально ждать — можно поставить wait_seconds = 3 для теста
            time.sleep(wait_seconds)

if __name__ == "__main__":
    try:
        session_loop()
    except KeyboardInterrupt:
        print("\n\nОстановлено пользователем (Ctrl+C).")