# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, color, name):
        self._max_speed = 120
        self.color = color
        self.name = name
        self._is_police = False

    def go(self, speed):
        if speed > 0:
            if speed < self._max_speed:
                print('{}{} автомобиль поехал вперед со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '', speed))
            else:
                speed = self._max_speed
                print('{}{} автомобиль поехал вперед с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',speed))
        elif speed < 0:
            if -speed < self._max_speed:
                print('{}{} автомобиль поехал назад со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',-speed))
            else:
                speed = -self._max_speed
                print('{}{} автомобиль поехал назад с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',-speed))
        else:
            print('{} автомобиль не поехал'.format(self.color))


    def stop(self):
        print('{}{} автомобиль остановился'.format(self.color, ' полицейский' if self._is_police else ''))

    def turn(self, direction):
        print('{}{} автомобиль повернул {}'.format(self.color, ' полицейский' if self._is_police else '',direction))

    def get_max_speed(self):
        return self._max_speed

    def get_is_police(self):
        return self._is_police


class SportCar:
    def __init__(self, color, name):
        self._max_speed = 350
        self.color = color
        self.name = name
        self._is_police = False

    def go(self, speed):
        if speed > 0:
            if speed < self._max_speed:
                print('{}{} автомобиль поехал вперед со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '', speed))
            else:
                speed = self._max_speed
                print('{}{} автомобиль поехал вперед с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',speed))
        elif speed < 0:
            if -speed < self._max_speed:
                print('{}{} автомобиль поехал назад со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',-speed))
            else:
                speed = -self._max_speed
                print('{}{} автомобиль поехал назад с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',-speed))
        else:
            print('{} автомобиль не поехал'.format(self.color))

    def stop(self):
        print('{}{} автомобиль остановился'.format(self.color, ' полицейский' if self._is_police else ''))

    def turn(self, direction):
        print('{}{} автомобиль повернул {}'.format(self.color, ' полицейский' if self._is_police else '', direction))

    def get_max_speed(self):
        return self._max_speed

    def get_is_police(self):
        return self._is_police

class WorkCar:
    def __init__(self, color, name):
        self._max_speed = 110
        self.color = color
        self.name = name
        self._is_police = False

    def go(self, speed):
        if speed > 0:
            if speed < self._max_speed:
                print('{}{} автомобиль поехал вперед со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '', speed))
            else:
                speed = self._max_speed
                print('{}{} автомобиль поехал вперед с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '', speed))
        elif speed < 0:
            if -speed < self._max_speed:
                print('{}{} автомобиль поехал назад со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '', -speed))
            else:
                speed = -self._max_speed
                print('{}{} автомобиль поехал назад с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '', -speed))
        else:
            print('{} автомобиль не поехал'.format(self.color))

    def stop(self):
        print('{}{} автомобиль остановился'.format(self.color, ' полицейский' if self._is_police else ''))

    def turn(self, direction):
        print('{}{} автомобиль повернул {}'.format(self.color, ' полицейский' if self._is_police else '', direction))

    def get_max_speed(self):
        return self._max_speed

    def get_is_police(self):
        return self._is_police

class PoliceCar:
    def __init__(self, color, name):
        self._max_speed = 200
        self.color = color
        self.name = name
        self._is_police = True

    def go(self, speed):
        if speed > 0:
            if speed < self._max_speed:
                print('{}{} автомобиль поехал вперед со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '', speed))
            else:
                speed = self._max_speed
                print('{}{} автомобиль поехал вперед с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',speed))
        elif speed < 0:
            if -speed < self._max_speed:
                print('{}{} автомобиль поехал назад со скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',-speed))
            else:
                speed = -self._max_speed
                print('{}{} автомобиль поехал назад с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self._is_police else '',-speed))
        else:
            print('{} автомобиль не поехал'.format(self.color))

    def stop(self):
        print('{}{} автомобиль остановился'.format(self.color, ' полицейский' if self._is_police else ''))

    def turn(self, direction):
        print('{}{} автомобиль повернул {}'.format(self.color, ' полицейский' if self._is_police else '', direction))

    def get_max_speed(self):
        return self._max_speed

    def get_is_police(self):
        return self._is_police


Car1 = TownCar('Желтый', 'Мерседес')
Car1.go(80)
Car1.go(140)
Car1.go(-10)
Car1.go(-130)
Car1.turn('направо')
Car1.turn('налево')
Car1.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car1.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car1.get_is_police() else 'гражданский'))

Car2 = SportCar('Красный', 'Феррари')
Car2.go(80)
Car2.go(400)
Car2.go(-50)
Car2.go(-360)
Car2.turn('направо')
Car2.turn('налево')
Car2.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car2.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car2.get_is_police() else 'гражданский'))

Car3 = WorkCar('Белый', 'Газель')
Car3.go(60)
Car3.go(130)
Car3.go(-5)
Car3.go(-120)
Car3.turn('направо')
Car3.turn('налево')
Car3.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car3.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car3.get_is_police() else 'гражданский'))

Car4 = PoliceCar('Синий', 'Форд')
Car4.go(60)
Car4.go(210)
Car4.go(-5)
Car4.go(-205)
Car4.turn('направо')
Car4.turn('налево')
Car4.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car4.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car4.get_is_police() else 'гражданский'))

print('-------Конец задачи 1-----------------------------------------------------------------')

# Задача - 2

# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Cars:
    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if speed > 0:
            if speed < self.max_speed:
                print('{}{} автомобиль поехал вперед со скоростью {} км/ч'.format(self.color, ' полицейский' if self.is_police else '', speed))
            else:
                speed = self.max_speed
                print('{}{} автомобиль поехал вперед с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self.is_police else '',speed))
        elif speed < 0:
            if -speed < self.max_speed:
                print('{}{} автомобиль поехал назад со скоростью {} км/ч'.format(self.color, ' полицейский' if self.is_police else '',-speed))
            else:
                speed = -self.max_speed
                print('{}{} автомобиль поехал назад с максимальной скоростью {} км/ч'.format(self.color, ' полицейский' if self.is_police else '',-speed))
        else:
            print('{} автомобиль не поехал'.format(self.color))

    def stop(self):
        print('{}{} автомобиль остановился'.format(self.color, ' полицейский' if self.is_police else ''))

    def turn(self, direction):
        print('{}{} автомобиль повернул {}'.format(self.color, ' полицейский' if self.is_police else '', direction))

    def get_max_speed(self):
        return self.max_speed

    def get_is_police(self):
        return self.is_police

class TownCar(Cars):
    def __init__(self, color, name):
        _max_speed = 125
        _is_police = False
        super().__init__(_max_speed, color, name, _is_police)

class SportCar(Cars):
    def __init__(self, color, name):
        _max_speed = 355
        _is_police = False
        super().__init__(_max_speed, color, name, _is_police)

class WorkCar(Cars):
    def __init__(self, color, name):
        _max_speed = 115
        _is_police = False
        super().__init__(_max_speed, color, name, _is_police)

class PoliceCar(Cars):
    def __init__(self, color, name):
        _max_speed = 205
        _is_police = True
        super().__init__(_max_speed, color, name, _is_police)


Car1 = TownCar('Желтый', 'Мерседес')
Car1.go(80)
Car1.go(140)
Car1.go(-10)
Car1.go(-130)
Car1.turn('направо')
Car1.turn('налево')
Car1.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car1.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car1.get_is_police() else 'гражданский'))

Car2 = SportCar('Красный', 'Феррари')
Car2.go(80)
Car2.go(400)
Car2.go(-50)
Car2.go(-360)
Car2.turn('направо')
Car2.turn('налево')
Car2.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car2.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car2.get_is_police() else 'гражданский'))

Car3 = WorkCar('Белый', 'Газель')
Car3.go(60)
Car3.go(130)
Car3.go(-5)
Car3.go(-120)
Car3.turn('направо')
Car3.turn('налево')
Car3.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car3.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car3.get_is_police() else 'гражданский'))

Car4 = PoliceCar('Синий', 'Форд')
Car4.go(60)
Car4.go(210)
Car4.go(-5)
Car4.go(-205)
Car4.turn('направо')
Car4.turn('налево')
Car4.stop()
print('Максимальная скорость автомобиля {} км/ч'.format(Car4.get_max_speed()))
print('Автомобиль {}'.format('полицейский' if Car4.get_is_police() else 'гражданский'))