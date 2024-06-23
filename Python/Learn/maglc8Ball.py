# подключил модуль рандом
import random
# написал функцию
def getAnswer (answerNumber):
    if answerNumber == 1:
        return 'It is certain - это точно'
    elif answerNumber == 2:
        return 'It is decidedly so - это решительно так'
    elif answerNumber == 3:
        return 'Yes - Да'
    elif answerNumber == 4:
        return 'Reply hazy try again - Ответ туманный попробуйте еще раз'
    elif answerNumber == 5:
        return 'Ask again later - Спросите позже снова'
    elif answerNumber == 6:
        return 'Concentrate and ask again - Собиритесь/сосредоточьтесь и спросите еще раз'
    elif answerNumber == 7:
        return 'My reply is no - Мой ответ нет'
    elif answerNumber == 8:
        return 'Outlook not so good - Перспективы не очень хорошие'
    elif answerNumber == 9:
        return 'Very doubtful - Очень сомнительно'
# создал переменную содержащую значение от 1 до 9 "randint возвращает значение с прописанными аргументами"
r = random.randint (1, 9)
# передаю значение переменной 'r' в функцию
fortune = getAnswer(r)
# вывожу значение
print (fortune)