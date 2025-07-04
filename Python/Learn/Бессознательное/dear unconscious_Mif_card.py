import random

def unconscious_answer(question):
    q = question.lower()

    # Блок обработки уточняющих вопросов
    if any(word in q for word in ["что это значит", "объясни", "поясни", "расшифруй", "уточни"]):
        return random.choice([
            "Подумай, к какой области твоей жизни это относится.",
            "Ответ приходит постепенно.",
            "Доверься своим внутренним ощущениям.",
            "Истинный смысл откроется в нужный момент.",
            "Вопрос уже несёт часть ответа."
        ])

    # Блок распознавания эмоциональной окраски
    if any(word in q for word in ["переживаю", "волнуюсь", "страх", "беспокойство", "паника", "тревога", "напряжение"]):
        return random.choice([
            "Сохраняй спокойствие.",
            "Эмоции — это естественно. Дай себе время.",
            "Глубокий вдох поможет сбалансироваться.",
            "Посмотри на ситуацию шире — всё устаканится.",
            "Будь добр к себе — ты справишься."
        ])

    # Блок распознавания нерешительности
    if any(word in q for word in ["стоит ли", "может быть", "вдруг", "не знаю", "что если", "сомневаюсь", "опасаюсь", "боюсь"]):
        return random.choice([
            "Доверься своим чувствам.",
            "Решение созреет со временем.",
            "Не бойся ошибок — опыт важен.",
            "Иногда важно сделать первый шаг.",
            "Ты знаешь больше, чем тебе кажется."
        ])

    if any(word in q for word in ["ехать", "поездка", "езда", "идти", "отправляться", "дорога", "путь", "путешествие", "отпуск", "поезжать"]):
        return random.choice(["Поезжай", "Лучше остаться дома", "Путь открыт", "Подумай ещё", "Отдых пойдёт на пользу"])
    elif any(word in q for word in ["покупать", "покупка", "покупаю", "купить", "приобрести"]):
        return random.choice(["Покупай", "Пока не стоит", "Подожди лучшего момента"])
    elif any(word in q for word in ["работать", "работа", "карьера", "труд", "занятие", "должность", "профессия", "увольнение"]):
        return random.choice(["Сосредоточься", "Не перегружай себя", "Работа даст плоды"])
    elif any(word in q for word in ["отношения", "любовь", "партнёр", "друг", "семья", "близкие", "брак", "развод", "общение", "разговаривать", "продолжать", "прекратить", "встречаться"]):
        return random.choice(["Будь честен", "Откройся", "Прислушайся к чувствам"])
    elif any(word in q for word in ["деньги", "финансы", "вложение", "инвестиции", "заработок", "доход", "прибыль"]):
        return random.choice(["Финансовый рост возможен", "Сейчас не лучшее время для вложений", "Будь осторожен в тратах"])
    elif any(word in q for word in ["здоровье", "болезнь", "самочувствие", "лечение", "симптом", "врач"]):
        return random.choice(["Позаботься о здоровье", "Обрати внимание на самочувствие", "Проконсультируйся со специалистом"])
    elif any(word in q for word in ["переезд", "смена города", "жильё", "квартира", "дом", "место жительства"]):
        return random.choice(["Переезд будет удачным", "Обдумай своё решение ещё раз", "Жди более подходящего момента"])
    elif any(word in q for word in ["духовность", "развитие", "предназначение", "путь", "медитация", "рост"]):
        return random.choice(["Доверяй своему пути", "Слушай сердце", "Продолжай внутренний рост"])
    elif any(word in q for word in ["учёба", "обучение", "курсы", "знания", "диплом", "университет"]):
        return random.choice(["Учиться всегда полезно", "Сейчас благоприятное время для обучения", "Продолжай развиваться"])
    elif any(word in q for word in ["дети", "ребёнок", "беременность", "материнство", "отцовство"]):
        return random.choice(["Ты готов к новому этапу", "Будь терпелив", "Решение созреет само"])
    else:
        return random.choice([
            "Доверься интуиции.", "Ответ внутри тебя.", "Пауза — тоже ответ.",
            "Это важнее, чем кажется.", "Позволь событиям развиваться естественно."
        ])

def main():
    print("Задай вопрос бессознательному (или введи 'выход' для завершения):")
    while True:
        question = input("Вопрос: ")
        if question.lower() == 'выход':
            print("До свидания!")
            break
        answer = unconscious_answer(question)
        print("Ответ бессознательного:", answer)

if __name__ == "__main__":
    main()
