from math import factorial


def triangle(number):
    l = [0] * (number + 1)
    for (index, _) in enumerate(l):
        l[index] += int((factorial(number)) / (factorial(index) * factorial(number - index)))    
    return l


print(triangle(0)) 
