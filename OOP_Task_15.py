# 15. Предприятие.
# Отдел: название, кол-во сотрудников.
# Сотрудник: ФИО, возраст, ЗП.
# - добавлять отдел, сотрудников,
# - удалять отделы, сотрудников,
# - редактировать отдел, сотрудников.
# При добавлении/удалении сотрудника в отдел, кол-во сотрудников должно увеличиваться/уменьшаться автоматически.
# Показывать всех сотрудников в отделе, все отделы, сумму зп в отделе.

class Company:

    def __init__(self, name):
        self.name = name
        self.departament_list = []

    def add_departament(self, *args):
        for departament in args:
            if isinstance(departament, Departament):
                self.departament_list.append(departament)

    def delete_departament(self, departament):
        if isinstance(departament, Departament):
            self.departament_list.remove(departament)

    def print_info(self):
        print('Компания "{}"\n\nОтделы компании:'.format(self.name))
        for departament in self.departament_list:
            print('- {}'.format(departament.name))


class Departament:

    def __init__(self, name):
        self.name = name
        self.employees_list = []

    def add_emploees(self, *args):
        for employee in args:
            if isinstance(employee, Employee):
                self.employees_list.append(employee)

    def delete_employees(self, employee):
        if isinstance(employee, Employee):
            self.employees_list.remove(employee)

    def print_info(self):
        print('\n{}. \nВ отделе сотрудников: {}, Общая ЗП: {} \nСписок сотрудников отдела:'.format(
            self.name, len(self.employees_list), sum([employee.salary for employee in self.employees_list])))

        for employee in self.employees_list:
            print('- {}'.format(employee.name))


class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def print_info(self):
        print('Имя сотрудника: {}\nВозраст сотрудника: {}\nЗарплата сотрудника: {}'.format(
            self.name, self.age, self.salary))


# Создаем объект "Предприятие" (экземпляр класса "Company"):
my_company = Company('Транспортная компания')

# Создаем объект "Отдел" (экземпляр класса "Departament"):
transport_departament = Departament('Транспортный отдел')
buy_departament = Departament('Отдел закупок')

# Добавляем отдел в предприятие (метод класса "Company"):
my_company.add_departament(transport_departament, buy_departament)
# my_company.add_departament(buy_departament)

# Создаем объект "Сотрудник" (экземпляр класса "Employee"):
employee_1 = Employee('Прометей Сергей Петрович', 55, 100000)
employee_2 = Employee('Вишнякова Елена Александровна', 23, 75000)
employee_3 = Employee('Иванова Мария Сергеевна', 30, 333333)
employee_4 = Employee('Степанов Игорь Эдуардович', 30, 111111)
employee_5 = Employee('Дубровин Максим Петрович', 30, 444444)

# Добавляем сотрудника в отдел (метод класса "Departament"):
buy_departament.add_emploees(employee_1, employee_2)
transport_departament.add_emploees(employee_3, employee_4, employee_5)


my_company.print_info()
transport_departament.print_info()
buy_departament.print_info()

transport_departament.delete_employees(employee_5)
my_company.delete_departament(buy_departament)

my_company.print_info()
transport_departament.print_info()
