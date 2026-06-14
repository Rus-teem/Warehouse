"""Сортировка элементов списка по типам и суммирование чисел."""

ab = [1, "2", 3, 4, "5"]

new_list3 = []
finalList = 0

for i in ab:
    if type(i) == int:
        new_list3.append(i)
        finalList += i
        print(new_list3)
print(finalList)
