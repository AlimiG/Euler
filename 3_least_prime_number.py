import time
start = time.time()
number = 600851475143

p = 2
while(p*p <= number):
    if (number%p == 0):
        number //= p
    else:
        p +=2 if p>2 else 1

print(number)
print(time.time()-start)

