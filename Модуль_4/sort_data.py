def sort_bubble(ls):
    '''
    Функция сортировки списка методом пузырька
    '''
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    return ls

def sort_selection(ls):
    '''
    Функция сортировки списка методом выборки
    '''
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
    return ls

def sort_insertion(ls):
    '''
    Функция сортировки списка методом вставки
    '''
    for i in range(1, len(ls)):
        item = ls[i]
        j = i - 1
        while j >= 0 and ls[j] > item:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = item
    return ls