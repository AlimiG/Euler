def lisofprimes(w):
    primes = []
    i = 0
    while i <= w :
        isprime = True
        for num in range (2 ,int(i**0.5)+1):
            if i % num == 0:
                isprime = False
                break

        if isprime:
            primes.append(i)
        i = i + 1
    return primes

primeslist = set(lisofprimes(1000000))

for i in primeslist.copy():
    for n in str(i):
        if int(n)==2 or int(n) == 4 or  int(n)==5 or int(n) == 6 or int(n) == 8 or int(n)==0:
            primeslist.remove(i)
            break

answer = {2,3,5,7}

for i in primeslist:
    stri = str(i)
    perms = [stri[i:]+stri[:i] for i in range(len(stri))]
    if all(int(i) in primeslist for i in perms):
        answer.add(i)

print(len(answer))