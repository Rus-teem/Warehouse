"""Извлечение телефонных номеров и email-адресов из буфера обмена."""

import re
import pyperclip


def extract_phone_numbers(text):
    """Извлекает телефонные номера из текста."""
    phone_pattern = re.compile(r"""(
        (\s|-|\.)*
        (\d)
        (\s|-|\.)?
        (\d{3}|\(\d{3}\))
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)?
        (\d{4}|\d{2})
        (\s|-|\.)?
        (\d{2})?
        (\s*(доб|доб.)\s*(\d{2,5}))?
    )""", re.VERBOSE)

    results = []
    for groups in phone_pattern.findall(text):
        phone_num = "-".join([groups[2], groups[4], groups[6], groups[8], groups[10]])
        if groups[11]:
            phone_num += " x" + groups[11]
        results.append(phone_num)
    return results


def extract_emails(text):
    """Извлекает email-адреса из текста."""
    email_pattern = re.compile(r"""(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})
    )""", re.VERBOSE)

    return [groups[0] for groups in email_pattern.findall(text)]


def main():
    """Читает текст из буфера обмена, извлекает номера и email-ы, копирует результат."""
    text = str(pyperclip.paste())

    phone_nums = extract_phone_numbers(text)
    emails = extract_emails(text)

    result = phone_nums + emails

    if result:
        pyperclip.copy("\n".join(result))
        print("Скопировано в буфер обмена.")
        print("\n".join(result))
    else:
        print("Телефонные номера и адреса электронной почты не обнаружены.")


if __name__ == "__main__":
    main()
