class House:
    def __init__(self, name, number_of_floors):
        # print('__init__')
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



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
