# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Задача-1
print('--- Задача 1 ---')
a = 0
b = 1
c = 5
print(a, b, c)
d = input('Введите любой текст или число: ')
print('Вы ввели ' + d)

# Задача-2
print('--- Задача 2 ---')
x = int(input('Введите число: '))
a = x + 2
print('Результат:', a)

# Задача-3
print('--- Задача 3 ---')
age=int(input('Введите Ваш возраст: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')