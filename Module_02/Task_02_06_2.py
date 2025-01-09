my_code = []
my_code_str = ''

number = int(input('Введите число в диапазоне от 3 до 20: '))

for i in range(1, int((number + 1) / 2)):
    for j in range(i + 1, number + 1):
        if number % (i + j) == 0 and i != j:
            my_code.append([i, j])
            my_code_str += str(i) + str(j)

print('Пары:', my_code)
print('Пароль: ', my_code_str)
