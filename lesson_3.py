# 1.
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
print("---------- 1 ----------")


def division(a, b):
    if b == 0:
        return 'Невозможно деление на ноль!' \
               '\nПопробуйте снова.'
    return round(a / b, 2)


a = int(input("Введите число которое будем делить: "))
b = int(input("Введите число на которое будем делить: "))

print(f"Результат деления: {division(a, b)}")

# 2.
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
print("---------- 2 ----------")


def about_yourself(dict_items):
    for i in dict_items: print(f"{i}: {dict_items[i]}")


dict_items = {'name': None, 'last name': None, 'year': None, 'city': None, 'email': None, 'number': None}
for item in dict_items:
    dict_items[item] = input(f"Enter your {item}, please: ")

about_yourself(dict_items)

# 3.
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
print("---------- 3 ----------")


def my_func(a, b, c):
    minimum = min([a, b, c])
    return sum([a, b, c]) - minimum


list_numbers = []
for i in range(1, 4):
    list_numbers.append(int(input(f"Введите число №{i}:")))

print(f"Сумма двух наибольших чисел: {my_func(list_numbers[0], list_numbers[1], list_numbers[2])}")

# 4.
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
print("---------- 4 ----------")


def my_func(x, y):
    return x ** y


def my_func_special(x, y):
    if y < 0:
        x = 1 / x
    new_x = x
    for i in range(1, abs(y)):
        new_x *= x
    return new_x


x = int(input("Введите число которое будем возводить в степень: "))
y = int(input("Введите степень в которую будем возводить: "))

print(f"Результат возведения в степень: {my_func(x, y)}")
print(f"*Результат возведения в степень: {my_func_special(x, y)}")

# 5.
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
print("---------- 5 ----------")


summ = 0
checker = True
while checker:
    str = input("Введите строку чисел: ")
    list_num = str.split(" ")
    for i in list_num:
        if i.isnumeric():
            summ += int(i)
        else:
            checker = False
    print(summ)

# 6.
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
print("---------- 6 ----------")


def int_func(line):
    return line.title()

print(int_func('test yes no'))