ab = [1, "2", 3, 4, "5"]

c = type(ab[0]) == int
print(c)


new_list = []
bagList = []
new_list2 = []
new_list3 = []
finalList = 0

for i in ab:
    if type(i) == int:
        new_list3.append(i)
        finalList += i
        print(new_list3)
print(finalList)

# for i in ab:
#     if isinstance(i, int):
#         new_list.append(i)
#         finalList +=i
#         print(new_list)
#     if isinstance(i, str):
#         new_list2.append(i)
#         print(new_list2, "сработало строки")
# print(finalList)
