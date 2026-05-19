import math 
import random
from abc import ABC, abstractmethod
from scipy.integrate import quad

class Calka(ABC):
    def __init__(self, f, a,b):
        self.f=f
        self.a=a
        self.b=b
    @abstractmethod
    def oblicz(self):
        pass

class Simpson(Calka):
    def __init__(self,f,a,b,n):
        super().__init__(f,a,b)
        self.n=n
    def oblicz(self):

        h=(self.b-self.a)/(2*self.n)
        s= self.f(self.a)+self.f(self.b)
        s+= 4*sum(self.f(self.a + (2*k-1)*h) for k in range(1, self.n+1))
        s+= 2*sum(self.f(self.a+(2*k*h)) for k in range (1, self.n))

        return s*h/3
    
class Probabilistic(Calka):
    def __init__(self, f, a, b, eps=1e-4):
        super().__init__(f, a, b)
        self.eps = eps

    def oblicz(self, true_value):
        s = 0
        n = 0
        while True:
            x = random.uniform(self.a, self.b)
            s += self.f(x)
            n += 1
            estimate = (self.b - self.a) * (s/n)
            if n > 100 and abs(estimate - true_value) < self.eps:
                return estimate, n
class MonteCarlo(Calka):
    def __init__(self, f, a, b, eps=1e-4):
        super().__init__(f, a, b)
        self.eps = eps

    def oblicz(self, true_value):
       
        xs = [self.a + i*(self.b - self.a)/1000 for i in range(1001)]
        ys = [self.f(x) for x in xs]
        ymin, ymax = min(ys), max(ys)

        area = (self.b - self.a) * (ymax - ymin)

        t = 0
        n = 0

        while True:
            x = random.uniform(self.a, self.b)
            y = random.uniform(ymin, ymax)
            fx = self.f(x)

            if 0 < y <= fx:
                t += 1
            elif 0 > y >= fx:
                t -= 1

            n += 1
            estimate = area * t / n

            if n > 100 and abs(estimate - true_value) < self.eps:
                return estimate, n           
f = lambda x: x*math.sin(x**2)
a,b=-3, 5

true_val,_ = quad(f,a,b)
print(true_val)

for n in [10,20,30,100]:
    val = Simpson(f,a,b,n).oblicz()
    print(f"n={n} , bland={abs(val-true_val)}")

prob_val, prob_n = Probabilistic(f, a, b).oblicz(true_val)
print("Wynik:", prob_val, "liczba losowań:", prob_n)
 

mc_val, mc_n = MonteCarlo(f, a, b).oblicz(true_val)
print("Wynik:", mc_val, "liczba losowań:", mc_n)
