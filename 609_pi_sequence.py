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
primes = sieve(10000)
def pi(n):
    j = 0
    summ = 0
    while j < n:
        j = primes[summ]
        summ = summ + 1 
    return (summ-1)

