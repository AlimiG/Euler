primes = []
i = 0
while len(primes) < 10003 :
    isprime = True
    for num in range (2 ,int(i**0.5)+1):
        if i % num == 0:
            isprime = False
            break

    if isprime:
        primes.append(i)
    i = i + 1


print(primes[10002])