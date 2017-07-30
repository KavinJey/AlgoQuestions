
from num2words import *


sum_1 = 0
for x in range(1, 1001):
    string = num2words(x)
    string = string.replace(" ", "")
    string = string.replace("-", "")
    number = len(string)
    sum_1 = sum_1 + number
    print sum_1, x, string

	
print sum_1
