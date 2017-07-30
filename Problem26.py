#reciprocal cycles
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from decimal import *
getcontext().prec = 100

list_of_numbers = []
list_1 = []

for x in range(3, 1001):
    if x % 2 == 0 or x % 5 ==0 and x % 3 != 0:
        continue

    else:
        decimal = Decimal(1) / Decimal(x)
        decimal = str(decimal)
        list_of_numbers.append(decimal)
        continue


#to do:
#function to find repeating cycles and quantifying them for about 1000 digits


for x in list_of_numbers:
    number = x.strip("0.")
    number = str(number)
    list_1.append(number)



#re-occuring patterns in strings
def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]


for x in list_of_numbers:
    if principal_period(x) != None:
        print(x)


#REAL ALGO FOR SOLUTION
"""
for (int i = 1000; i > 1; i--) {
    if (sequenceLength >= i) {
        break;
}

int[]
foundRemainders = new
int[i];
int
value = 1;
int
position = 0;

while (foundRemainders[value] == 0 & & value != 0) {
    foundRemainders[value] = position;
    value *= 10;
    value %= i;
    position++;
}

if (position - foundRemainders[value] > sequenceLength) {
    sequenceLength = position - foundRemainders[value];
    }
}"""