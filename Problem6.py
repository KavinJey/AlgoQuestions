#Find the difference between the sum of squares of the first one hundred
#natural numbers and the square of the sum

def sum_of_number():
    sum_numbers = 0 
    for x in range(1, 101):
        sum_numbers = sum_numbers + x**2
        print x
    return sum_numbers

def square_of_sum():
    sum_numbers = 0
    for x in range(1, 101):
        sum_numbers = sum_numbers + x
    sum_numbers = sum_numbers**2
    return sum_numbers 

sum1 = sum_of_number()
sum2 = square_of_sum()

print "the difference is", sum2 - sum1
