#В переменную example запишите любую строку.
example = 'Топинамбур'

#Выведите на экран(в консоль) первый символ этой строки.
print(example[0])

#Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
print(example[-1])

#Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
print(example[len(example)//2::1])

#Выведите на экран(в консоль) это слово наоборот.
print(example[::-1])

#Выведите на экран(в консоль) каждый второй символ этой строки.
print(example[1::2])