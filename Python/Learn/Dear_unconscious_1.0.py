import random  # Импортируем модуль random для генерации случайных чисел

# Функция, которая возвращает "Да" или "Нет" в зависимости от переданного числа
def unconscious(answerNumber):
    if answerNumber == 1:
        return "Да"
    elif answerNumber == 2:
        return "Нет"

# Генерируем случайное число: 1 или 2
randNumber = random.randint(1, 2)

# Получаем ответ бессознательного (Да или Нет)
answerUnconscious = unconscious(randNumber)

# Выводим сообщение о начале работы
print("Узнай готово ли бессознательное к разговору и хочет это произойти сейчас")
print("Бессознательно хочет ответить: " + answerUnconscious)

# Функция, которая обрабатывает следующий шаг в зависимости от ответа бессознательного
def nextStep(answerUnconscious):
    if answerUnconscious == 'Да':
        print("Задай свой вопрос:")
        su = input()  # Получаем ввод пользователя
        return su
    elif answerUnconscious == "Нет":
        print("Попробуй в следующий раз")

# Запускаем функцию nextStep с полученным ответом бессознательного
nextStep(answerUnconscious)
import random  # Импортируем модуль random для генерации случайных чисел
import time  # Для добавления паузы ожидания
import sys  # Для красивого вывода без переноса строки
from datetime import datetime  # Для отображения времени ожидания

# Функция для генерации готовности бессознательного
def unconscious_ready():
    return random.choice(["Да", "Нет"])

# Функция, которая отвечает на вопрос пользователя
def unconscious_answer():
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
        wait_minutes = random.randint(1, 3)  # Для демонстрации: ожидание 1–3 минуты
        print(f"Бессознательное не готово. Следующая попытка через {wait_minutes} минут...")

        for remaining in range(wait_minutes, 0, -1):
            current_time = datetime.now().strftime("%H:%M:%S")
            sys.stdout.write(f"\r[{current_time}] Ожидание: осталось {remaining} минут... ")
            sys.stdout.flush()
            time.sleep(60)
        print()Lj