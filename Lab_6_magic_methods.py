import random
import numpy

class Airplane:
    
    def __init__(self, planetype, destination, weekday, flightnum, flighttime):
        self.planetype=planetype #Тип самолета
        self.destination=destination # направление, пункт назначения
        self.flightnum=flightnum #номер рейса, 
        self.weekday=weekday    #Дни недели
        self.flighttime=flighttime    #Время вылета, .
    
        
    def __str__(self):
        return "тип -"+str(self.planetype) +" направление - "+ str(self.destination)+" день недели -"+str(self.weekday)

    
    @staticmethod
    def getinfo(): 
        types=['boing', 'airbus', 'superjet']
        cities=['Paris', 'London', 'Amsterdam']
        l = [1, 2, 3, 4, 5, 6, 7]
        print(f"введите модель самолета ")
        a=input()
        print(f"введите город назначения")
        b=input()
        print(f"введите день недели рейса")
        c=int(input())
        if a in types and b in cities and int(c) in l:
            print("введите номер рейса")
            d=input()
            print("введите время рейса")
            e=input()
            return Airplane(a, b, c, d, e)
        else:
            print("ошибка ввода")

    def CheckCity(self,city): #Проверка направления-города
        if self.destination==city:
            return 1
        else:
            return 0
    
    def CheckWeekday(self, d): #Проверка дня недели
        if self.weekday==d:
           # return [self.planetype, self.flightnum] #возвращает список полетов - тип самолета и номер полета
            return self
            
    def __repr__(self):                 # магический метод 5
        return f'Airplane(planetype={self.planetype},destination={self.destination}, flightnum={self.flightnum}, weekday={self.weekday},weekday={self.flighttime})'
        



    
class AirplaneList:         #	Класс-список рейсов 
    def __init__(self):
        self.list = []
    
    def __str__(self):
        return self.list

    def append(self, ob):
        self.list.append(ob)

    def __getitem__(self, index): #	1. Магический метод получения объекта из списка
        return self.list[index] 
        
    def __len__(self):              #	2. Магический метод получения длины списка-класса
        return len(self.list)

    def __lt__(self, other):            #	3. Сравнение списков (меньше)
        return len(self)<len(other)

    def __eq__(self, other):        #	4. Сравнение списков  (равенство)
        return len(self)==len(other)
    



planeList = AirplaneList()

plane1=Airplane.getinfo()
plane2=Airplane.getinfo()
planeList.append(plane1)
planeList.append(plane2)

plane3=Airplane("boing", "Paris", 3, "ff", "10.00")
plane4=Airplane("airbus", "Paris", 4, "ff", "10.00")
planeList.append(plane3)
planeList.append(plane4)

print("вы ввели данные о")
a=int(planeList.__len__())
for i in range(a):
    print(planeList.__getitem__(i)) # Вывод


#количество полетов в  Paris

s1=0
a=int(planeList.__len__())
for i in range(a):
    s1=s1+(planeList.__getitem__(i)).CheckCity("Paris")
print(f"{s1} - количество полетов в  Paris")

# список рейсов для заданного дня недели

print(f"введите день недели")
d=int(input())

                        #полеты для дня недели
i=0
a=int(planeList.__len__())
for i in range(a):
    #print((planeList.__getitem__(i)).CheckWeekday(d))
    
    if (planeList.__getitem__(i)).CheckWeekday(d)!=None:
        print(planeList.__getitem__(i))


print('Проверка работы магических методов, добавление полетов в списки и сравнение списков')

listParis= AirplaneList()
listLondon= AirplaneList()

for item in planeList:
    city = getattr(item, 'destination')
    if city=='Paris':
        listParis.append(item)
    if city=='London':
        listLondon.append(item)    

print('полеты в Париж')
for item in listParis:    
    print(item)
    
print('полеты в Лондон')
for item in listLondon:    
    print(item)
    
x=listLondon.__lt__(listParis)
print(f'полетов в Лондон меньше чем полетов в Париж - {x}')

x=listLondon.__eq__(listParis)
print(f'полетов в Лондон равно количеству полетов в Париж - {x}')

print(f'список всех полетов - repr')
for item in planeList:
    print(item.__repr__())



