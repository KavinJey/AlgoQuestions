

h = int(input())
m = int(input())

t = 1

for x in range(241):
    A = -6*(t)**4 + h*(t)**3 + 2*(t)**2 + t
    t += 1
    if A <= 0 or t > m:
        break

if t > m:
    print("The balloon does not touch ground in the given time.")

if t < m:
    print("The balloon first touches ground at hour:\n", t-1)