"""Магический шар 8 — случайное предсказание."""

import random


def getAnswer(answerNumber):
    """Возвращает предсказание по номеру ответа (1-9)."""
    answers = {
        1: 'It is certain - это точно',
        2: 'It is decidedly so - это решительно так',
        3: 'Yes - Да',
        4: 'Reply hazy try again - Ответ туманный попробуйте еще раз',
        5: 'Ask again later - Спросите позже снова',
        6: 'Concentrate and ask again - Соберитесь/сосредоточьтесь и спросите еще раз',
        7: 'My reply is no - Мой ответ нет',
        8: 'Outlook not so good - Перспективы не очень хорошие',
        9: 'Very doubtful - Очень сомнительно',
    }
    return answers.get(answerNumber, 'Error')


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
