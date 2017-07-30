#If largest palindrome made from product of two 2-digit numbers is
#9009 = 91 * 99 then what is the largest palindrome made from
#product of 3-digit numbers


global list_of_numbers
list_of_numbers = []

#checks if palindrome
def palindrome(number):
    
    if number[0] == number[5]:
        if number[1] == number[4]:
            if number[2] ==  number[3]:
                return True
    else:
        return False
    
#finds products of 3-digit numbers  
def products():
    for x in range(900, 1000):
    
        for b in range(900, 1000):
            
            product = x * b
            product = str(product)
            
            
            number = []
            
            for i in product:
                number.append(i)
             

                
            condition = palindrome(product)
            
            if condition == True:
                global list_of_numbers
                list_of_numbers.append(product)


    


products() 

final = len(list_of_numbers) - 1 
print "biggest palindrome:",  list_of_numbers[final]


