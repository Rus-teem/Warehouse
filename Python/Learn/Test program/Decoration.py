"""Пример использования декоратора в Python."""


def frame_decorator(func):
    """Декоратор: обрамляет вывод функции рамкой из звёздочек."""
    def wrapper():
        print("*" * 10)
        func()
        print("*" * 10)
    return wrapper


@frame_decorator
def greet():
    print("прикольно!")


def bye():
    print("Пока!")


greet()
print("\n")
bye()
