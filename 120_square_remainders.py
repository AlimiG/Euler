
import numpy as np
import time
start = time.time()
maxi = []
for i in range(3,1001):
    a = []
    for n in range(1100):
        num = ((i-1)**n)+((i+1)**n)
        a.append(num % i**2)
    maxi.append(max(a))

print(sum(maxi))

print(time.time()-start)