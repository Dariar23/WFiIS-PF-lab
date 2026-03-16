################ Zadanie 1

def for_list(f):
    def new_function(list):
        list_after=[]
        for elem in list:
            list_after.append(f(elem))
        return list_after
    return new_function
def x2(x):
    return (x + 2) * x

lx2 = for_list(x2)
d = [2, 4, 5, 0.56]
r = lx2(d)
print(r)



############# Zadanie 2


orders = [{"product": "Laptop", "price": 3000, "quantity": 1}, 
        {"product": "Smartphone", "price": 800, "quantity": 5}, 
        {"product": "Headphones", "price": 200, "quantity": 5},
        {"product": "Mouse", "price": 150, "quantity": 1}, ]


def filter_by_min_value(min_value):
    def filter_function(order):
        return (order["price"]*order["quantity"] >= min_value)
    return filter_function

filtered_orders = list(filter(filter_by_min_value(1000), orders))
print(filtered_orders)


##############Zadanie 3

def decorator_memorization(function):
    memory = {}

    def wrapper(x):
        if x in memory:
            return memory[x]

        result = function(x)
        memory[x] = result
        return result

    return wrapper


@decorator_memorization
def kwadrat(a):
    return a * a


@decorator_memorization
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(kwadrat(8))   
print(kwadrat(x=3))  
print(factorial(3))   
