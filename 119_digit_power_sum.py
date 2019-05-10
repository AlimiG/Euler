import time
import math
start = time.time()
"""def summ(n):
    summ = 0
    for i in str(n):
        summ = summ + int(i)
    return summ

def check(first):
    n = summ(first)
    if n!=1:
        x = math.log(first,100)/ math.log(n,100)
        if (n**int(x)) == first:
            return True
        else:
            return False
    else:
        return False

sequence = []
for i in range(11,400000):
        if check(i):
            sequence.append(i)

print(sequence)
print(len(sequence))
"""
print(sum(map(int,list(str(2**1000)))))




print(time.time()-start)

