#Find the 10 001st prime number
#first 6 primes are: 2, 3, 5, 7, 11 and 13

condition = True
primes = 6
interger = 14
 
#works for every prime number above 10 
def prime(number):
    count = 1
    for x in range(2, number):
        divisible = number % x

        if divisible > 0:
            count = count + 1
 
    if count == number-1:
        return True
    
    else:
        return False 
    

while condition == True:
    
   
    value = prime(interger)
    
    if value == True:
        primes = primes + 1
        print "ding", primes 
        if primes == 10001:
            condition = False
            print interger
        
    interger = interger + 1
    
