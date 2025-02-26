# Генератор числе Трибоначи

import numpy

def tribonachi_generator(n):
    A: list[int]=[0, 0, 1]
    while len(A)<n:
        i=A[-1]+A[-2]+A[-3]
        A.append(i)
        yield i
        
gen_iter=tribonachi_generator(35)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))

# класс с объектом итератором Трибоначи



class TribonachiGen:
    
    def __iter__(self):
        return self
        
    def __init__(self, limit):    
        self.limit=limit
        self.counter=0
        self.list = [0, 0, 1]
        
    def __next__(self):
        if self.counter<self.limit:
            i=self.list[-1]+self.list[-2]+self.list[-3]
            self.list.append(i)
            self.counter+=1
            return i
        else:
            raise StopIteration
            
        
    def __str__(self):
        return self.A
            
        
gen1=TribonachiGen(35)
for j in gen1:
    print(j)