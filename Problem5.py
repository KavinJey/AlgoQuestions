#2520 is the smallest number that can be divided
#by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is
#evenly divisible by all of the numbers from 1 to 20?

number = 11617840
set_condition = True


while set_condition == True:     
    for x in range(21, 1, -1):
        if number % x==0: 
            print number
            if x == 1:
                smallest_number = number
                set_condition = False
                print "ha fucking gay"
        else:
            break
   
    number = number + 20

print "This is it", smallest_number
