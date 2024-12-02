#1. Задайте кортеж из переменных разных типов данных:
immutable_var=(1 ,2, 3, 2.2, 10.1, 'Вася', 'Коля', True, [1,2], [3,5])

#2. Вывести кортеж immutable_var на экран:
print(immutable_var)

#3. Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#immutable_var[0]=2 #--->TypeError: 'tuple' object does not support item assignment

#4. Создайте переменную mutable_list и присвойте ей список из нескольких элементов.:
mutable_list= [1 ,2, 3, 2.2, 10.1, 'Вася', 'Коля', True, [1,2], [3,5]]

#5. Измените элементы списка mutable_list.
mutable_list[0]=10
mutable_list[5]='Петя'

#6. Выведите на экран измененный список mutable_list.
print(mutable_list)