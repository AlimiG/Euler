import time
start = time.time()
fac_table = {0: 1} #Using cachetable
def factorial(n):
    if n not in fac_table:
        fac_table[n] = n*factorial(n-1)
    return fac_table[n]
listy = []
for i in range(3,1000000):
    summ = 0
    for j in str(i):
        summ = summ + factorial(int(j))
    if summ == i :
        listy.append(i)

print(listy)
print(sum(listy))

print(time.time() - start)
