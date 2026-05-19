import random

class LCG:
    def __init__(self,seed=1):
        self.m= 2**31 -1
        self.a=7**5
        self.c=0
        self.x=seed

    def __iter__(self):
        return self
    
    def __next__(self):
        self.x=(self.a*self.x +self.c)%self.m
        return self.x / self.m
    
def test_generate(gen):
    it =iter(gen)
    N = 100000

    pairs =[(next(it), next(it)) for _ in range(N)]

    result ={}
    for n in range(1,11):
        side=0.1**n
        result[n]=sum( 1 for x,y in pairs if x<= side and y <=side) / N *100
    return result

def test_random():
    N=100000
    pairs = [(random.random(), random.random()) for _ in range(N)]
    return {n : sum(1 for x, y in pairs if x<= 0.1**n and y <= 0.1**n) / N*100 for n in range(1,11)}

if __name__=="__main__":
    lcg = test_generate(LCG())
    print(lcg)
    py_test=test_random()
    print(py_test)
