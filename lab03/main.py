from math import cos
#dla zad 2
def generator(func, x, dx):
    #new_value = func(x)
    #print(new_value)
    #yield new_value
    while(True):
        if (abs(x-func(x)) < dx):
            break
        x=func(x)
        yield x
#dla zad 3
def operation(a: int, b: int , operation:str):
    if operation == '-':
        return a-b
    if operation == '+':
        return a+b
    if operation =='*':
        return a*b
    if operation == '/':
        return a/b
    
def reduce(expression):
   
    if isinstance(expression, (int, int)):
        return expression
    
    left, operator, right = expression
    
    left_value = reduce(left)
    right_value = reduce(right)
    
    return operation(left_value, right_value, operator)

#######zad 1 
a = ['hello', '0', 'to 2 centy', 'x', 'but o nr 44', '3 wilgi' ]

wynik_1 = list(map(lambda indeks_napis: indeks_napis[1], filter(lambda indeks_napis: str(indeks_napis[0]) in indeks_napis[1],enumerate(a))))
print(list(wynik_1))
########zad 2
globalA = 3
test_1 = list(generator(lambda x: cos(x), 0.3, 0.4))
test_2 = list(generator(lambda x: 1 + 1 / x, 0.6, 2))
test_3 = list(generator(lambda x: (x + globalA / x) / 2, 0.5, 1))
print(f"{test_1}\n{test_2}\n{test_3}")


##########zad 3

e = ((1,'+', 6), '*', (2,'+', 7)) 
print(reduce(e))