my_code = []
my_code_str = ''

number = int(input('Введите число в диапазоне от 3 до 20: '))

for i in range(2, number + 1):
    if number % i == 0:
        for j in range(1, int((i + 1) / 2)):
            pair_1 = j
            pair_2 = i - j
            # Не понял, почему нельзя брать пары одинаковых чисел, например для 6 - 3+3 тоже является делителем! - Пусть будет, как в ТЗ)
            # В противном случае, условие в строке 16 надо убрать.
            if pair_1 != pair_2:
                my_code.append([pair_1, pair_2])
                my_code_str += str(pair_1) + str(pair_2)

print('Пары:', my_code)
print('Пароль: ', my_code_str)
