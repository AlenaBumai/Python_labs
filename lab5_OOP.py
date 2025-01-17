import random
import numpy


class Table:
    __mass = 0

    def __init__(self, mass0):
        self.__mass = mass0

    def __str__(self):
        return "стол весом " + str(self.__mass)

    # чтение инкапсулированной массы
    def get_mass(self):
        return self.__mass


# журнальный стол
class JournalTable(Table):
    storage = 0


# обеденный стол
class DinnerTable(Table):
    __places = 0

    def __init__(self, mass0):
        Table.__init__(self, mass0)
        self.__places = mass0 // 5

    # чтение инкапсулированного числа мест
    def get_places(self):
        return self.__places


class Truck:
    __maxMass = 0
    __tables = []

    def __init__(self, max_mass):
        self.__maxMass = max_mass

    def addTable(self, m):
        Total = 0
        for i in self.__tables:
            print(i)
            Total += i.get_mass()

        if self.__maxMass >= (Total + m):
            self.__tables.append(Table(m))
            print("загружено")
        else:
            print("превышение")


Truck1 = Truck(100)
Truck1.addTable(40)
Truck1.addTable(40)
Truck1.addTable(40)