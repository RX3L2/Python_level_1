# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class Toy:
    def __init__(self, name, colour, type):
        self.name = name
        self.colour = colour
        self.type = type


class Factory_toys:
    def __init__(self, name, colour, type):
        self.name = name
        self.colour = colour
        self.type = type

    def purchase(self):
        print('Сырье закуплено для {}, цвет {}, {}'.format(self.name, self.colour, self.type))

    def sewing(self):
        print('Игрушка {} сшита'.format(self.name))

    def colouring(self):
        print('Игрушка {} окрашена в {} цвет'.format(self.name, self.colour))

    def factory_run(self):
        self.purchase()
        self.sewing()
        self.colouring()
        return Toy(self.name, self.colour, self.type)


factory1 = Factory_toys('Крокодил', 'зеленый', 'животное')
toys_1 = factory1.factory_run()
print(toys_1.name, toys_1.colour, toys_1.type)


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


