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


class Animal_toy(Toy):
    def __init__(self, name, colour):
        type = 'животное'
        super().__init__(name, colour, type)


class Mult_persona_toy(Toy):
    def __init__(self, name, colour):
        type = 'персонаж мультфильма'
        super().__init__(name, colour, type)

class Factory_toys_new(Factory_toys):
    def __init__(self, name, colour, type):
        super().__init__(name, colour, type)

    def factory_run(self):
        self.purchase()
        self.sewing()
        self.colouring()

        return Animal_toy(self.name, self.colour) if self.type == 'Animal' else Mult_persona_toy(self.name, self.colour)

print('----- Задача - 2 ------')
factory2 = Factory_toys_new('Крокодил', 'зеленый', 'Animal')
toys_2 = factory2.factory_run()
print(toys_2.name, toys_2.colour, toys_2.type)

factory3 = Factory_toys_new('Смешарик', 'синий', 'Mult')
toys_3 = factory3.factory_run()
print(toys_3.name, toys_3.colour, toys_3.type)