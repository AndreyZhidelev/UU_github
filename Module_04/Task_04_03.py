import random

import Module_04.sort_data

a = Input('Начнем?', color='green')

# Создание списка произвольных значений
n = random.randint(10, 20)
data = []
for i in range(n):
    data.append(random.randint(-20, 20))

print(f'Исходный список: {data = }')

# Сортировка списка разными методами
print('Метод пузырька:', Module_04.sort_data.sort_bubble(data))
print('Метод вставки:', Module_04.sort_data.sort_insertion(data))
print('Метод выборки:', Module_04.sort_data.sort_selection(data))
