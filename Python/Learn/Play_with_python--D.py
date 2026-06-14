"""Эксперименты с основами Python: строки, числа, функции."""

text = "hello"
txt2 = 5 == int(len('hello'))
txt3 = len(str(str(45)+'hi'))
txt4 = 4 == 4 and 4 != 5 or 'tex'=='tex'


def hello(name, name2):
    """Выводит приветствие с переданными именами."""
    print('Привет!' + name + name2)
    print('Привет!!!')
    print('Привет всем.' + name)


hello(' python', str(54 + 3.124))

print("Привет тут дальше дописали ", end="")
print(text, txt2, txt3, txt3 + txt2, txt4)
