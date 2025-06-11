import sys  # Для красивого вывода без переноса строки
from datetime import datetime  # Для получения текущего времени
import random  # Импортируем модуль random для генерации случайных чисел
import time  # Для добавления паузы ожидания

# Функция для генерации готовности бессознательного
def unconscious_ready():
    return random.choice(["Да", "Нет"])

# Функция, которая отвечает на вопрос пользователя
def unconscious_answer():
    return random.choice(["Да", "Нет", "Попробуй позже", "Не сейчас", "Ответ скрыт", "Это важно для тебя", "Доверься интуиции"])

# Главный цикл — позволяет вести несколько вопросов за сессию
print("Добро пожаловать в режим диалога с бессознательным 2.0!")
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
        wait_minutes = random.randint(15, 30)
        print(f"Бессознательное не готово. Следующая попытка через {wait_minutes} минут...")
        
        for remaining in range(wait_minutes, 0, -1):
            current_time = datetime.now().strftime("%H:%M:%S")
            sys.stdout.write(f"\r[{current_time}] Ожидание: осталось {remaining} минут... ")
            sys.stdout.flush()
            time.sleep(60)
        print()
