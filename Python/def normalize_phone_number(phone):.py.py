import re

# Функция для нормализации номера телефона к формату +7XXXXXXXXXX
def normalize_phone_number(raw):
    # Удаляем все символы, кроме цифр (включая пробелы, скобки, тире и т.д.)
    digits = re.sub(r'\D', '', raw)
    
    # Пропускаем строки, если нет цифр или длина не 10–11 символов
    if not digits or len(digits) not in [10, 11]:
        return None

    # Если номер из 11 цифр и начинается на 8 — заменяем на +7
    if len(digits) == 11 and digits.startswith('8'):
        return '+7' + digits[1:]
    # Если номер из 11 цифр и начинается на 7 — добавляем +
    elif len(digits) == 11 and digits.startswith('7'):
        return '+7' + digits[1:]
    # Если номер из 10 цифр — добавляем +7 в начало
    elif len(digits) == 10:
        return '+7' + digits
    else:
        return None

# Открываем файл с номерами телефонов для чтения ('r' — режим чтения)
# 'with' — контекстный менеджер, автоматически закрывает файл после работы
# encoding='utf-8' — указывает кодировку файла для корректного чтения символов
with open('/Users/rustem/Documents/Project files/Code file/Phone_number.txt', 'r', encoding='utf-8') as file:
    # Читаем строки из файла, применяя line.strip() для удаления пробелов и символов переноса строки
    # Игнорируем пустые строки (line.strip() возвращает пустую строку, если строка пустая)
    numbers = [line.strip() for line in file if line.strip()]

# Применяем нормализацию к каждому номеру, сохраняя пустые строки для невалидных номеров
normalized = [
    normalize_phone_number(num) or '' for num in numbers
]

# Открываем файл для записи ('w' — режим записи, перезаписывает файл)
# 'with' — контекстный менеджер, автоматически закрывает файл после работы
# encoding='utf-8' — указывает кодировку файла для корректной записи символов
with open('/Users/rustem/Documents/Project files/Code file/Normalized_phones.txt', 'w', encoding='utf-8') as out_file:
    # Записываем каждый нормализованный номер построчно
    for number in normalized:
        out_file.write(number + '\n')