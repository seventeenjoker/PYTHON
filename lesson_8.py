
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
print("*" * 50 + " 1 " + "*" * 50)


class Data:
    @classmethod
    def set_date(cls, date):
        if Data.validate(date):
            day, month, year = date.split('-')
            print(f"{int(day)} - {int(month)} - {int(year)}")


    @staticmethod
    def validate(date):
        i = 3
        try:
            day, month, year = date.split('-')
            if int(day) > 31 or int(day) < 1:
                print('День не валидный')
                i -= 1
            if int(month) > 12 or int(month) < 1:
                print('Месяц не валидный')
                i -= 1
            if int(year) > 2050 or int(year) < 1900:
                print('Год не валидный')
                i -= 1
        except ValueError:
            print("Введите дату в формате дд-мм-гггг.")
            return False
        if i == 3:
            return True


Data.set_date("1-12-2020")

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна 
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
print("*" * 50 + " 2 " + "*" * 50)


class MyOwnException(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите делимое: ")
b = input("Введите делитель: ")


if int(b) == 0:
    raise MyOwnException("Делитель не должен быть равен 0!")
try:
    result = int(a) / int(b)
except ValueError:
    print("Введите числа!")

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. 
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, 
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) 
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
print("*" * 50 + " 3 " + "*" * 50)

class NewException:
    def __init__(self, *args):
        self.my_list = []

    def income_value(self):
        while True:
            try:
                value = input("Введите число: ")
                value = int(value)
                self.my_list.append(value)
                print(f"Список введенных значений: {self.my_list}")
            except:
                print("Введите только число!")
                Y_N = input("Продолжим? Введите Да/Нет")
                if Y_N.lower() == "да":
                    print(try_1.income_value())
                else:
                    print("До свидания!")
                    break

try_1 = NewException(0)
print(try_1.income_value())


"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. 
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП.
"""
print("*" * 50 + " 4-5-6 " + "*" * 50)


class Office:
    total_dict = {}

    def __init__(self, name, cost, speed_per_sec, count):
        self.name = name
        self.cost = cost
        self.speed_per_sec = speed_per_sec
        self.count = count
        if Office.validate_data(self.cost, self.count):
            self.total_dict = {"Наименование": self.name, "Цена за единицу": self.cost, "Количество ед.": self.count}

    def move_to_storage(self):
        if self.total_dict:
            print(f"Передано на склад: {self.total_dict}")


    @staticmethod
    def validate_data(cost, count):
        try:
            cost = int(cost)
            count = int(count)
            return True
        except ValueError:
            "Введены некорректные даннные для цены или количества."


class Printer(Office):
    def __init__(self, name, cost, speed_per_sec, type, count):
        super().__init__(name, cost, speed_per_sec, count)
        self.type = type
        self.move_to_storage()


class Scanner(Office):
    def __init__(self, name, cost, speed_per_sec, count):
        super().__init__(name, cost, speed_per_sec, count)
        self.move_to_storage()


class Xerox(Office):
    def __init__(self, name, cost, speed_per_sec, count):
        super().__init__(name, cost, speed_per_sec, count)
        self.move_to_storage()


printer_1 = Printer("Принтер HP", 25000, 30, "Черно-белый", 6)
printer_2 = Printer("Принтер Canon", 30000, 40, "Цветной", 5)
scanner_1 = Scanner("Сканер HP", 10000, 10, 10)


"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""
print("*" * 50 + " 7 " + "*" * 50)


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print("Сумма a и b равна:")
        return f"z = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        print(f'Произведение a и b равно:')
        return f"z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i"

    def __str__(self):
        return f"z = {self.a} + {self.b} * i"


complex_1 = ComplexNumber(3, 1)
complex_2 = ComplexNumber(-1, -2)
print(complex_1)
print(complex_1 + complex_2)
print(complex_1 * complex_2)

