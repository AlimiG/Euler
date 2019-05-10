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
def leftoright(a):
    for i in range(len(str(a))-1):
        if a in primes:
            if str(a)[1:] != '':
                a = int(str(a)[1:])
    if (len(str(a))-1) == 0 :
        return True
    else:
        return False


def rightoleft(a):
    for i in range(len(str(a))-1):
       if a in primes:
           a = int(str(a)[:-1])
    if (len(str(a))-1)==0 :
        return True
    else:
        return False

listy = []
for i in primes:
    if leftoright(i) and rightoleft(i):
        listy.append(i)

print(listy)
print(sum(listy))



#print(leftoright(1542))
print(time.time()-start)