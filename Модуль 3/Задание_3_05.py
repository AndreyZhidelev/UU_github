def get_multiplied_digits(number):
    str_number = str(number)
    n = len(str_number)
    first = int(str_number[0:1])
    if first != 0:
        if n > 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first
    else:
        return 1


N = 402030
print(get_multiplied_digits(N))
