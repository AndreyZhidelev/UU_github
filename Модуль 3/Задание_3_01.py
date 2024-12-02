calls = 0


def count_calls():
    # Функция, подсчитывающая вызовы остальных функций
    global calls
    calls += 1
    return calls


def string_info(string):
    # Функция принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    n = len(string)
    UCaseStr = string.upper()
    LCaseStr = string.lower()
    return (n, UCaseStr, LCaseStr)


def is_contains(string, list_to_search):
    # Функция принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
    # False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    count_calls()
    if string.casefold() in (item.casefold() for item in list_to_search):
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('ArMaViR'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycleng', 'cyclic']))  # No matches
print(is_contains('Avi', ['AV', 'Garage', 'Aviation']))  # 1 matches
print(calls)


На вот тебе