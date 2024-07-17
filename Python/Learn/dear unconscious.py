import random


def unconscious(answerNumber):
    if answerNumber == 1:
        return "Да"
    elif answerNumber == 2:
        return "Нет"


randNumber = random.randint(1, 2)

answerUnconscious = unconscious(randNumber)

print("Узнай готово ли бессознательное к разговору")
print("Бессознательно хочет ответить: " + answerUnconscious)

def nextStep (answerUnconscious):
    if answerUnconscious == 'Да':
        print("Задай свой вопрос:")
        su = input()
        return su
    elif answerUnconscious == "Нет":
        print("Попробуй в следующий раз")

# nextStep(answerUnconscious)
readinessResponse = nextStep(answerUnconscious)

print(readinessResponse)


