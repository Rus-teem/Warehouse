import numpy as np

statusPersent = np.array([1.68, 0.66, 1.9, 3.28, 7.51, 8.75])
arrStatusPersent = np.mean(statusPersent)
print("mean of arr : ", round(arrStatusPersent, 2))
print("Среднее значение : ", round(np.average(statusPersent), 3))
print("Сумма : ", int(statusPersent.sum()))
print("Максимадбное число : ", statusPersent.max())
