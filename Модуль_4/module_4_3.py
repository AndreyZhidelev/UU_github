import random

import Модуль_4.sort_data
from Модуль_4.sort_data import *

# Создание списка произвольных значений
n = random.randint(10, 20)
data = []
for i in range(n):
    data.append(random.randint(-20, 20))

print(f'Исходный список: {data = }')

# Сортировка списка разными методами
print('Метод пузырька:', Модуль_4.sort_data.sort_bubble(data))
print('Метод вставки:', Модуль_4.sort_data.sort_insertion(data))
print('Метод выборки:',Модуль_4.sort_data.sort_selection(data))