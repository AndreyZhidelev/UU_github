def calculate_structure_sum(data):
    N = 0
    # если элемент - строка
    if isinstance(data, str):
        N += len(data)
    # если элемент - число типа int или float
    elif isinstance(data, (int, float)):
        N += data
    # если элемент - список, кортеж или множество
    elif isinstance(data, (list, tuple, set)):
        for elem in data:
            N += calculate_structure_sum(elem)
    # если элемент - словарь
    elif isinstance(data, (dict)):
        for key_, value_ in data.items():
            if isinstance(key_, str):
                N += len(key_)
            elif isinstance(key_, (int, float)):
                N += key_
            N += calculate_structure_sum(value_)
    return N

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
