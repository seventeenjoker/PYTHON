import random
import json

"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
print("*" * 50 + " 1 " + "*" * 50)

with open('5_1.txt', 'w') as file:
    name = input('Введите свое имя: ')
    file.write(name + '\n')
    last_name = input('Введите свою фамилию: ')
    file.write(last_name + '\n')


"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
print("*" * 50 + " 2 " + "*" * 50)

with open('5_2.txt', 'r', encoding='utf-8') as file_1:
    print(f"Количество строк в файле: {sum(1 for line in file_1)}")

with open('5_2.txt', 'r', encoding='utf-8') as file_2:
    something_list = 0
    for line in file_2:
        something_list += len(line.split())
    print(f"Количество слов в файле: {something_list}")


"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
print("*" * 50 + " 3 " + "*" * 50)

empl_dict = {}

with open('5_3.txt', 'r', encoding='utf-8') as file_3:
    for line in file_3:
        empl_dict[line.split()[0]] = float(line.split()[1])
        if float(line.split()[1]) < 20000:
            print(f"Зарплата меньше 20000 у {line.split()[0]}: {float(line.split()[1])}")

max_salary = max(empl_dict.values())
employee = {k:v for k, v in empl_dict.items() if v == max_salary}
print(employee)

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
print("*" * 50 + " 4 " + "*" * 50)

f = open('5_result.txt', 'w')
f.close()

with open('5_4.txt', 'r', encoding='utf-8') as file_4:
    for line in file_4:
        if 'One' in line:
            line = line.replace('One', 'Один')
        elif 'Two' in line:
            line = line.replace('Two', 'Два')
        elif 'Three' in line:
            line = line.replace('Three', 'Три')
        elif 'Four' in line:
            line = line.replace('Four', 'Четые')
        with open('5_result.txt', 'a', encoding='utf-8') as file_4_:
            file_4_.write(line)


"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
print("*" * 50 + " 5 " + "*" * 50)

f = open('5_5.txt', 'w')
f.close()

rand_line = []
for i in range(1, 21):
    rand_line.append(int(random.random() * 100))

with open('5_5.txt', 'a', encoding='utf-8') as file_5:
    for i in rand_line:
        file_5.write(str(i) + " ")
    file_5.close()

with open('5_5.txt', 'r', encoding='utf-8') as file_5_2:
    list_from_file = []
    for line in file_5_2:
        list_from_file += line.split()
    print(f"Сумма чисел в файле: {sum(int(i) for i in list_from_file)}")


"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                     Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
print("*" * 50 + " 6 " + "*" * 50)

lessons_dict = {}
with open('5_6.txt', 'r', encoding='utf-8') as file_6:
    for line in file_6:
        sum = 0
        for i in range(1, 4):
            try:
                int(line.split()[i])
                sum += int(line.split()[i])
            except ValueError:
                pass
        lessons_dict[line.split()[0]] = sum

print(lessons_dict)


"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
print("*" * 50 + " 7 " + "*" * 50)

firm_dict = {}
with open('5_7.txt', 'r', encoding='utf-8') as file_7:
    for line in file_7:
        firm_info = line.replace('\n', '').split(';')
        firm_dict[firm_info[0]] = float(firm_info[1]) - float(firm_info[2])

print(f"Прибыть кадой компании: {firm_dict}")
print(f"Средняя прибыль компаний: {sum(firm_dict.values()) / len(firm_dict.keys())}")

data_for_json = {'income': firm_dict, 'average_profit': sum(firm_dict.values()) / len(firm_dict.keys())}
print(data_for_json)
with open("my_file_.json", "w", encoding='utf-8') as write_f:
    json.dump(data_for_json, write_f)
