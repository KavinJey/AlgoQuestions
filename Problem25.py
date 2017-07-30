#Fibonnacci sequence term with 1000 digits

global x1
x1 = 1
global x2
x2 = 1

list_1 = []
list_1.append(str(x1))
list_1.append(str(x2))

#smh make a better fibo function that returns the value of the new term
def fibo_nac():
    global x1, x2
    x3 = x1  + x2
    x1 = x2
    x2 = x3
    return x3

while True:
    print(x1, x2)
    fibo_nac()
    list_1.append(str(x2))
    if len(list_1[len(list_1) - 1]) >= 1000:
        print(list_1[len(list_1) - 1])
        break

print(len(list_1))