import time
start = time.time()
cache = {1: 1}
def collatz_count(n):
        if n not in cache:
                if n%2 ==0:
                        cache[n] = 1 +collatz_count(n/2)
                else:
                        cache[n] = 1 +collatz_count(3*n+1)
        return cache[n]

seed = 0
biggest = 0
"""
for i in range(1,1000001):
        a = collatz_count(i)
        if a > biggest:
                biggest = a
                seed = i
"""

print(collatz_count(837799))

print(time.time() - start)