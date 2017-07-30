#Digit Factorials
from math import *
import math

def check_sum(n):
    string = str(n)
    sum_num = 0

    for x in string:
        number = int(x)
        number = math.factorial(number)
        sum_num += number

    if sum_num == n:
        return True

    else:
        return False


sum_total = 0

for x in range(3, 1500000):
    print(x, check_sum(x))
    if check_sum(x) == True:
        sum_total += x


print(sum_total)
40730