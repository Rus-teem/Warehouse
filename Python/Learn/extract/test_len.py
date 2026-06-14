"""Демонстрация подсчёта длины списка через len() и собственную функцию."""

mob_place = [
    "ru.bestfeeds.vk-feed",
    "com.yandex.browser",
]

run1 = len(mob_place)
print(run1)


def findLen(arr):
    """Подсчитывает количество элементов в списке без использования len()."""
    counter = 0
    while arr[counter:]:
        counter += 1
    return counter


print(findLen(mob_place))
