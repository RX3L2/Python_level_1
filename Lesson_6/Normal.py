# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, clan, damage=20, health=200, armor=1.5):
        self.name = name
        self.clan = clan
        self.damage = damage
        self._health = health
        self.armor = armor
        print('Создан {} по имени {} с уроном {} здоровьем {} и броней {}'.format(self.clan, self.name, self.damage,
                                                                                  self._health, self.armor))

    def get_health(self):
        return self._health

    def _damage_calculate(self, who_attaks):
        self._health -= round(who_attaks.damage / self.armor, 0)

    def attack(self, who):
        print('{} {} пошел в атаку на {} {}'.format(who.clan, who.name, self.clan, self.name))
        self._damage_calculate(who)
        print('У {} {} осталось {} здоровья'.format(self.clan, self.name, self._health))


class Player(Person):
    def __init__(self, name, clan, damage, health, armor):
        super().__init__(name, clan, damage, health, armor)
        print('{} {} является игроком'.format(clan, name))


class Enemy(Person):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        print('{} {} является врагом'.format(clan, name))


class Game:
    def __init__(self, gamer_1, gamer_2):
        self.gamer_1 = gamer_1
        self.gamer_2 = gamer_2

    def run_game(self):
        print('Приветствуем на игре {} и {}'.format(self.gamer_1.name, self.gamer_2.name))
        while True:

            if self.gamer_1.get_health() > 0:
                self.gamer_2.attack(self.gamer_1)
            else:
                print('Игра окончена, {} {} проиграл'.format(self.gamer_1.clan, self.gamer_1.name))
                break
            if self.gamer_2.get_health() > 0:
                self.gamer_1.attack(self.gamer_2)
            else:
                print('Игра окончена, {} {} проиграл'.format(self.gamer_2.clan, self.gamer_2.name))
                break

gamer = Player('Василий', 'эльф', 15, 150, 1.2)
bot = Enemy('Дори', 'гном')
gaming = Game(gamer, bot)
gaming.run_game()
