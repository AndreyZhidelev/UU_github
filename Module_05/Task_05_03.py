class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor_by_floor = ''
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                if i != new_floor:
                    floor_by_floor += str(i) + ', '
                else:
                    floor_by_floor += str(i)
        else:
            floor_by_floor = 'Такого этажа не существует'
        print(f'Жилой комплекс "{self.name}": Этажи: {floor_by_floor}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if not isinstance(self, int):
            raise TypeError("Количество этажей должно быть задано целым числом!")

        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

# # __eq__
# print(h1 == h2)
#
# # __add__
# h1 = h1 + 10
# print(h1)
# print(h1 == h2)
#
# # __iadd__
# h1 += 10
# print(h1)
#
# # __radd__
# h2 = 10 + h2
# print(h2)
#
# # __gt__
# print(h1 > h2)
#
# # __ge__
# print(h1 >= h2)
#
# # __lt__
# print(h1 < h2)
#
# # __le__
# print(h1 <= h2)
#
# # __ne__
# print(h1 != h2)

