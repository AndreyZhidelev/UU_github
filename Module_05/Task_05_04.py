class House:
    houses_history = []

    def __new__(cls, name, number_of_floors):
        # print('__new__')
        cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        # print('__init__')
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{str(self.name)} снесён, но он останется в истории')
        # House.houses_history.remove(self.name) --> Если надо удалить элемент из списка

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

    def __add__(self, value):
        if not isinstance(value, (int, House)):
            raise ArithmeticError("Количество этажей должно быть задано типом int или объектом House!")
        s_value = value if isinstance(value, int) else value.number_of_floors
        self.number_of_floors += s_value
        return self

    def __iadd__(self, value):
        # Вариант решения 1
        # if not isinstance(value, (int, House)):
        #     raise ArithmeticError("Количество этажей должно быть задано типом int или объектом House!")
        # sc = value if isinstance(value, int) else value.number_of_floors
        # self.number_of_floors += sc
        # return self

        # Вариант решения 2
        self.__add__(value)
        return self

    def __radd__(self, value):
        # # Вариант решения 1
        # if not isinstance(value, (int, House)):
        #     raise ArithmeticError("Количество этажей должно быть задано типом int или объектом House!")
        # sc = value if isinstance(value, int) else value.number_of_floors
        # self.number_of_floors += value
        # return self

        # Вариант решения 2
        self.__add__(value)
        return self


#Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)
