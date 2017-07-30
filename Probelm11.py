condition = True
primes = 19243571082
interger = 706210

#need more efficient prime number algorithm
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
    
def addition():
    prime(interger)
    if prime(interger) == True:
        return interger 
    
    
while condition == True:
    
   
    value = prime(interger) 
    if value == True:
        some_int = addition()
        primes = some_int + primes
        print "ding" 
        if interger == 2000000:
            condition = False
            print interger, "sum is", primes
        
    interger = interger + 1
