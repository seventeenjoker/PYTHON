import time

"""
1.
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только 
в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение 
и завершать скрипт.
"""
print("*" * 50 + " 1 " + "*" * 50)


class TrafficLight:
    __color = ['red', 'yellow', 'green']
    timeout = 10

    def running(self):
        while self.timeout:
            print(f"{time.strftime('%H:%M:%S')} {self.__color[0]}")
            time.sleep(7)
            print(f"{time.strftime('%H:%M:%S')} {self.__color[1]}")
            time.sleep(2)
            print(f"{time.strftime('%H:%M:%S')} {self.__color[2]}")
            time.sleep(4)
            print(f"{time.strftime('%H:%M:%S')} {self.__color[1]}")
            time.sleep(2)
            self.timeout -= 1
            print(self.timeout)


new_light = TrafficLight()
new_light.running()


"""
2.
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""
print("*" * 50 + " 2 " + "*" * 50)

class Road():
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width
        self.weight(self._length, self._width)

    def weight(self, _length, _width, weight=25, depth=0.005):
        try:
            _length = int(_length)
            _width = int(_width)
            if _length < 0 or _width < 0:
                print("Введите положительные числа для расчета")
            else:
                print(f"Расчет массы асфальта: {_length * _width * weight * depth} тонн.")
        except ValueError:
            print("Введите числа для расчета")


road = Road(20, 5000)


"""    
3.
Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров).
"""
print("*" * 50 + " 3 " + "*" * 50)


class Worker():
    _income = {"Зарплата": 100000, "Бонус": 50000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self.get_full_name()
        self.get_total_income()

    def get_full_name(self):
        print(f"Сотрудник: {self.name} {self.surname} на позиции: {self.position}")

    def get_total_income(self):
        print(f"Зарплата работника: {sum(self._income.values())}")


new_position = Position('Ivan', 'Ivanov', 'java developer')


"""    
4.
Реализуйте базовый класс Car. 
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).  
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""
print("*" * 50 + " 4 " + "*" * 50)


class Car:
    def __init__(self, speed, color, name, is_police, speed_limit):
        self.speed = speed
        self.color = color
        self.name = name
        self.speed_limit = speed_limit
        self.is_police = is_police
        self.go()

    def go(self):
        print(f"{self.name} проехала на скорости {self.speed}!...")

    def stop(self):
        print(f"Машина {self.name} запарковалась...")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False, speed_limit=60):
        super().__init__(speed, color, name, is_police, speed_limit)

    def go(self):
        print(f"{self.name} проехала на скорости {self.speed}!...")
        if self.speed > self.speed_limit:
            print(f"Превышение скорости на {self.speed - self.speed_limit}!")
            police_car = PoliceCar(120, 'black', 'bmw')
            self.turn('right')
            self.stop()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False, speed_limit=200):
        super().__init__(speed, color, name, is_police, speed_limit)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False, speed_limit=40):
        super().__init__(speed, color, name, is_police, speed_limit)

    def go(self):
        print(f"{self.name} проехала на скорости {self.speed}!...")
        if self.speed > self.speed_limit:
            print(f"Превышение скорости на {self.speed - self.speed_limit}!")
            police_car = PoliceCar(120, 'black', 'bmw')
            self.stop()



class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True, speed_limit=250):
        super().__init__(speed, color, name, is_police, speed_limit)

    def go(self):
        print("--!Выезжаем за нарушителями ПДД.")


town_car_1 = TownCar(60, 'red', 'Volkswagen polo')
town_car_2 = TownCar(80, 'blue', 'Volkswagen passat')
sport_car_1 = SportCar(120, 'black', 'Peugeot L500 R Hybrid Concept')
work_car_1 = WorkCar(60, 'white', 'Kia rio')
work_car_1 = WorkCar(35, 'orange', 'Kia Picanto')
sport_car_2 = SportCar(120, 'gris aluminium', 'Citroen C4 Sedan Exclusive')


"""
5.
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
print("*" * 50 + " 5 " + "*" * 50)


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        pass


class Pen(Stationery):
    def __init__(self, title='Ручка'):
        super().__init__(title)

    def draw(self):
        print(f"Используем {self.title} что бы нарисовать жирафа.")


class Pencil(Stationery):
    def __init__(self, title='Карандаш'):
        super().__init__(title)

    def draw(self):
        print(f"Используем {self.title} что бы нарисовать природу.")


class Handle(Stationery):
    def __init__(self, title='Маркер'):
        super().__init__(title)


    def draw(self):
        print(f"Используем {self.title} для разукрашивания.")


pen_1 = Pen()
pencil_1 = Pencil()
handle_1 = Handle()

pen_1.draw()
pencil_1.draw()
handle_1.draw()