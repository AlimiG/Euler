import time
start = time.time()

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5) +1):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = []
    for i in range(n):
        if is_prime[i] == True:
            prime.append(i)
    return prime

primes = sieve(1000000)

def proper_divisors(n):
        divisors = []
        i = 1
        while i <= n/2:
                if n%i == 0:
                        divisors.append(i)
                i+=1
        divisors.append(n)
        return divisors 


numees = []
for i in range(1,100001):
    final = True
    while final:
        for j in proper_divisors(i):
            if j not in primes:
                final = False
    if final:
        numees.append(i)

print(numees)



print(time.time()-start)