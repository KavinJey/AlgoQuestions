#A Pythagorean triplet is a set of three natural numbers,
#a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#02/14/17, Jeyakavin Jeyaranjan

#get things that add to 1000
from math import *


a = 3
b = a + 1
c = sqrt(a**2 + b**2)

def check():
    if a + b + c == 1000:
        return True
    else:
        return False

for x in range(1, 1001):
    a = x
    for e in range(1 , 1001):
        b = e
        c = sqrt(a**2 + b**2)
        condition = check()
        print(a, b, c, condition)
        if condition == True:
            break

    if condition == True:
        break

