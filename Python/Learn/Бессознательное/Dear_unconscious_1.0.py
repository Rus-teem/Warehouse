"""Диалог с бессознательным: версии 1.0 (простой) и 1.5 (циклический диалог)."""

import random
import time
import sys
from datetime import datetime


def unconscious(answerNumber):
    """Возвращает 'Да' или 'Нет' в зависимости от числа (1 или 2)."""
    if answerNumber == 1:
        return "Да"
    elif answerNumber == 2:
        return "Нет"


def nextStep(answerUnconscious_v1):
    """Запрашивает вопрос, если бессознательное готово."""
    if answerUnconscious_v1 == 'Да':
        print("Задай свой вопрос:")
        q = input()
        return q
    else:
        print("Попробуй в следующий раз")


# === Версия 1.0 ===
randNumber = random.randint(1, 2)
answerUnconscious_v1 = unconscious(randNumber)
print("Узнай готово ли бессознательное к разговору")
print("Бессознательно хочет ответить: " + answerUnconscious_v1)
nextStep(answerUnconscious_v1)

print("\n" + "="*50 + "\n")

# === Версия 1.5 ===

def unconscious_ready():
    """Случайным образом определяет готовность бессознательного."""
    return random.choice(["Да", "Нет"])


def unconscious_answer():
    """Возвращает случайный ответ бессознательного."""
    return random.choice([
        "Да", "Нет", "Попробуй позже", "Не сейчас",
        "Ответ скрыт", "Это важно для тебя", "Доверься интуиции"
    ])


print("Добро пожаловать в режим диалога с бессознательным 1.5!")
print("Чтобы выйти из программы — введи 'выход' в любой момент.\n")

while True:
    readiness = unconscious_ready()
    print("Готово ли бессознательное к разговору? ->", readiness)

    if readiness == "Да":
        while True:
            question = input("Задай свой вопрос: ")
            if question.strip().lower() == "выход":
                print("Сеанс завершён. До новых встреч!")
                sys.exit()
            answer = unconscious_answer()
            print("Ответ бессознательного:", answer)

            continue_dialog = input("Хочешь задать ещё вопрос? (да/нет): ").strip().lower()
            if continue_dialog != "да":
                print("Сеанс завершён. До новых встреч!")
                sys.exit()
    else:
        wait_minutes = random.randint(1, 3)
        print(f"Бессознательное не готово. Следующая попытка через {wait_minutes} минут...")

        for remaining in range(wait_minutes, 0, -1):
            current_time = datetime.now().strftime("%H:%M:%S")
            sys.stdout.write(f"\r[{current_time}] Ожидание: осталось {remaining} минут... ")
            sys.stdout.flush()
            time.sleep(60)
        print()
