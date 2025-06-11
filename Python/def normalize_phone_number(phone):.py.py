import re

# Скрипт для нормализации списка телефонных номеров.
# - Поддерживает различные форматы ввода: с пробелами, скобками, тире, и т.п.
# - Приводит все корректные номера к формату +7XXXXXXXXXX.
# - Для некорректных или отсутствующих номеров вставляет пустую строку.
# - Сохраняет соответствие количества строк между исходным и выходным файлами.
# - Входной и выходной файлы задаются абсолютными путями.

# Функция для нормализации номера телефона к формату +7XXXXXXXXXX
def normalize_phone_number(raw):
    # Удаляем все символы, кроме цифр (включая пробелы, скобки, тире и т.д.)
    digits = re.sub(r'\D', '', raw)

    # Если меньше 10 цифр — пропускаем
    if len(digits) < 10:
        return None

    # Если 10 цифр — добавляем +7
    if len(digits) == 10:
        return '+7' + digits

    # Если 11 цифр и начинается с 8 или 7 — заменяем первую цифру на +7
    if len(digits) == 11:
        if digits.startswith('8') or digits.startswith('7'):
            return '+7' + digits[1:]

    # Всё остальное пропускаем
    return None

# Открываем файл с номерами телефонов для чтения ('r' — режим чтения)
# 'with' — контекстный менеджер, автоматически закрывает файл после работы
# encoding='utf-8' — указывает кодировку файла для корректного чтения символов
with open('/Users/rustem/Documents/Project files/Code file/Phone_number.txt', 'r', encoding='utf-8') as file:
    # Читаем строки из файла, применяя line.strip() для удаления пробелов и символов переноса строки
    numbers = [line.strip() for line in file]


# Применяем нормализацию к каждому номеру, сохраняя пустые строки для невалидных номеров
normalized = [
    normalize_phone_number(num) or '' for num in numbers
]

# Подсчёт статистики
total = len(numbers)
success = sum(1 for num in normalized if num)
empty = sum(1 for num in normalized if not num)

# Вывод статистики в консоль
print(f"Всего строк обработано: {total}")
print(f"Успешно нормализовано: {success}")
print(f"Пустых строк (некорректных номеров): {empty}")

# Открываем файл для записи ('w' — режим записи, перезаписывает файл)
# 'with' — контекстный менеджер, автоматически закрывает файл после работы
# encoding='utf-8' — указывает кодировку файла для корректной записи символов
with open('/Users/rustem/Documents/Project files/Code file/Normalized_phones.txt', 'w', encoding='utf-8') as out_file:
    # Записываем каждый нормализованный номер построчно
    for number in normalized:
        out_file.write(number + '\n')