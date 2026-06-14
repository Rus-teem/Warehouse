"""Нормализация телефонных номеров к формату +7XXXXXXXXXX."""

import re


def normalize_phone_number(raw):
    """Приводит номер телефона к формату +7XXXXXXXXXX."""
    digits = re.sub(r'\D', '', raw)
    if len(digits) < 10:
        return None
    if len(digits) == 10:
        return '+7' + digits
    if len(digits) == 11:
        if digits.startswith('8') or digits.startswith('7'):
            return '+7' + digits[1:]
    return None


def main():
    """Читает номера из файла, нормализует и сохраняет результат."""
    input_path = '/Users/rustem/Documents/Project files/Code file/Phone_number.txt'
    output_path = '/Users/rustem/Documents/Project files/Code file/Normalized_phones.txt'

    with open(input_path, 'r', encoding='utf-8') as file:
        numbers = [line.strip() for line in file]

    normalized = [normalize_phone_number(num) or '' for num in numbers]

    total = len(numbers)
    success = sum(1 for num in normalized if num)
    empty = sum(1 for num in normalized if not num)

    print(f"Всего строк обработано: {total}")
    print(f"Успешно нормализовано: {success}")
    print(f"Пустых строк (некорректных номеров): {empty}")

    with open(output_path, 'w', encoding='utf-8') as out_file:
        for number in normalized:
            out_file.write(number + '\n')


if __name__ == "__main__":
    main()
