"""primes = []
i = 0
sumo = 0
while i < 2000000 :
    isprime = True
    for num in range (2 ,int(i**0.5)+1):
        if i % num == 0:
            isprime = False
            break

    if isprime and (i<2000000):
        sumo = sumo + i
    i = i + 1

print(sumo)
"""
import itertools
def check_permutations(num):
    y = []
    k = list(str(num))
    r = list(itertools.permutations(k))
    for i in r:
        number = ""
        for j in i:
            number = number + j  
        y.append(int(number))
    return y

print(len(set(check_permutations(3))))