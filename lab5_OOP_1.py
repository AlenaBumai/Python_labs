import random
import numpy


class Airplane:

    def __init__(self, planetype, destination, weekday, flightnum, flighttime):
        self.planetype = planetype  # Тип самолета
        self.destination = destination  # направление, пункт назначения
        self.flightnum = flightnum  # номер рейса,
        self.weekday = weekday  # Дни недели
        self.flighttime = flighttime  # Время вылета, .

    def __str__(self):
        return "тип -" + str(self.planetype) + " направление - " + str(self.destination) + " день недели -" + str(
            self.weekday)

    @staticmethod
    def getinfo():
        types = ['boing', 'airbus', 'superjet']
        cities = ['Paris', 'London', 'Amsterdam']
        l = [1, 2, 3, 4, 5, 6, 7]
        print(f"введите модель самолета ")
        a = input()
        print(f"введите город назначения")
        b = input()
        print(f"введите день недели рейса")
        c = input()
        if a in types and b in cities and int(c) in l:
            print("введите номер рейса")
            d = input()
            print("введите время рейса")
            e = input()
            return Airplane(a, b, c, d, e)
        else:
            print("ошибка ввода")

    #	список рейсов для заданного пункта назначения

    @classmethod
    def c(cls):
        cls.count += 1

    def CheckCity(self, city):  # Проверка направления-города
        if self.destination == city:
            return 1
        else:
            return 0

    def CheckWeekday(self, d):  # Проверка дня недели
        if self.weekday == d:
            return [self.planetype, self.flightnum]  # возвращает список полетов - тип самолета и номер полета


plane1 = Airplane.getinfo()
plane2 = Airplane.getinfo()
# plane3=Airplane("boing", "Paris", 3, "ff", "10.00")
# plane4=Airplane("airbus", "Paris", 4, "ff", "10.00")

print("вы ввели данные о")
print(plane1)
print(plane2)
Arr = [plane1, plane2]


def A(array):
    return array[1]


s1 = 0
print(A(Arr))
Arr[0].CheckCity("Paris")
for i in range(len(Arr)):
    s1 = s1 + Arr[i].CheckCity("Paris")
print(f"{s1} - количество полетов в  Paris")

# список рейсов для заданного дня недели

FlightListForDay = []  # полеты для 4 дня недели
for i in range(len(Arr)):
    if Arr[i].CheckWeekday(4) != None:
        FlightListForDay.append(Arr[i].CheckWeekday(4))
print(FlightListForDay)



