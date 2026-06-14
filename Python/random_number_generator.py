import random
import sys


def generate_random_number(min_value: int = 0, max_value: int = 100) -> int:
    # Проверяем корректность диапазона перед генерацией.
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
    # Возвращаем случайное целое число в заданных границах.
    return random.randint(min_value, max_value)


if __name__ == "__main__":
    # Читаем аргументы командной строки: start и end.
    args = sys.argv[1:]

    if len(args) == 2:
        start = int(args[0])
        end = int(args[1])
    else:
        # Значения по умолчанию, если диапазон не передан.
        start = 0
        end = 100

    print(generate_random_number(start, end))
