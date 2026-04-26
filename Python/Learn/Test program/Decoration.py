def frame_decorator(func):
    def wrapper():
        print("*" * 10)
        func()  # Вызываем исходную функцию
        print("*" * 10)
    return wrapper

# Применяем декоратор
@frame_decorator
def greet():
    print("прикольно!")

# @frame_decorator
def bye():
    print("Пока!")

# @frame_decorator
def probel():
    print(" \n "*2)

greet()  # Вывод: рамка + Привет! + рамка

probel()

bye()    # Вывод: рамка + Пока! + рамка