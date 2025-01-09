from math import inf

def divide(first, second):
    '''
    Функция деления по правилам высшей математики
    :param first:
    :param second:
    :return:
    '''
    if second == 0:
        return inf
    else:
        return first / second

