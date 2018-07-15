# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

print('Задание - 1')

def info_to_str(name, age, city):
    str = '{}, {} год(а), проживает в городе {}'.format(name, age, city)
    return (str)

name = 'Иван'
age = 30
city = 'Кемерово'
print(info_to_str(name, age, city))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

print('Задание - 2')

def max_num(num1, num2, num3):
    return max(num1, num2, num3)

print(max_num(34, 78, -90))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

print('Задание - 3')

def max_length_str(*arguments):
    max_length = 0
    for a in range(len(arguments)):
        if len(arguments[a]) > max_length:
            max_length = len(arguments[a])
            max_string = arguments[a]
    return max_string

print(max_length_str('qwerty', '1455789', '1234567890', 'абвгдеёжзикл'))
