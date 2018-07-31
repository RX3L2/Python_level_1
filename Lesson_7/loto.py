#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Gamer():
    def __init__(self, name):
        self._numbers = self._new_card()
        self._name = name

    def _new_card(self):
        card_list = []
        list_numbers = [x for x in range(1, 91)]
        for i in range(3):
            position = random.sample([x for x in range(0, 9)], 5)
            value = random.sample(list_numbers, 5)
            value.sort()
            column = []
            for j in range(9):
                if j in position:
                    list_numbers.remove(value[0])
                    column.append(value.pop(0))

                else:
                    column.append('*')
            card_list += column

        return card_list

    def remove_number(self, number):
        if number in self._numbers:
            i = self._numbers.index(number)
            self._numbers[i] = '-'

    def get_name(self):
        return self._name

    def get_card(self):
        card = []
        for i in range(3):
            for j in range(9):
                card.append(self._numbers[9*i+j])
        return card

    def print_card(self):
        print('Карточка игрока {}'.format(self._name))
        for i in range(3):
            for j in range(9):
                print(str(self._numbers[9*i+j]).rjust(3, ' '), end='')
            print('')



class Game():
    def __init__(self, user_name, bot_name):
        self._keg_in_game = [x for x in range(1, 91)]
        self._current_keg = 0
        self.gamer_user = Gamer(user_name)
        self.gamer_bot = Gamer(bot_name)

    def get_keg(self):
        self._current_keg = random.sample(self._keg_in_game, 1)[0]
        self._keg_in_game.remove(self._current_keg)
        return self._current_keg

    def run_game(self):
        print('Игрок {} и {} начали игру'.format(self.gamer_user.get_name(), self.gamer_bot.get_name()))

        while len(self._keg_in_game) > 0:
            self.gamer_user.print_card()
            self.gamer_bot.print_card()
            self._current_keg = self.get_keg()
            print('Выпал бочонок с номером: {}'.format(self._current_keg))
            print('Осталось бочонков в мешке: {}'.format(len(self._keg_in_game)))
            action = input('Зачеркнуть цифру? (y/n)')

            if self._current_keg in self.gamer_user.get_card():
                if action == 'y':
                    print('Игра продолжается, {} зачеркнул цифру'.format(self.gamer_user.get_name()))
                    self.gamer_user.remove_number(self._current_keg)
                else:
                    print('{} проиграл, необходимо было зачеркнуть цифру :-('.format(self.gamer_user.get_name()))
                    break
            else:
                if action != 'y':
                    print('Игра продолжается, цифры не было у {} в карточке'.format(self.gamer_user.get_name()))
                else:
                    print('Вы проиграли, такой цифры нет у {} на карточке :-('.format(self.gamer_user.get_name()))
                    break

            if self._current_keg in self.gamer_bot.get_card():
                print('{} зачеркнул цифру'.format(self.gamer_bot.get_name()))
                self.gamer_bot.remove_number(self._current_keg)

            else:
                print('У {} не было такой цифры'.format(self.gamer_bot.get_name()))



            if self.gamer_user.get_card().count('-') >= 15:
                print('Выиграл {}'.format(self.gamer_user.get_name()))
                break
            if self.gamer_bot.get_card().count('-') >= 15:
                print('Выиграл {}'.format(self.gamer_bot.get_name()))
                break

        else:
            print('В мешке больше не осталось бочонков!!!')


game_loto = Game('Пользователь', 'Компьютер')
game_loto.run_game()
