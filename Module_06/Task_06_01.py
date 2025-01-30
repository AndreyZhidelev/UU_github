class Animal():
    alive = True    # живой / мертвый
    fed = False     # название животного

    def __init__(self, name):
        self.name = name   # название животного

    def eat(self, food):
        if food.edible == True:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')

class Plant():
    edible = False

    def __init__(self, name):
        self.name = name   # название цветка

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True

#Выполняемый код(для проверки):

# Создаем объекты
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик-семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

# Кушаем разные растения
a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
