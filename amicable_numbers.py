def proper_divisors(n):
    listi = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            listi.append(i)
    return sum(listi)


amicable = []
numbers = list(range(0,10001))
for i in numbers:
    c = proper_divisors(i)
    if proper_divisors(c) == i:
        if c!=i:
            amicable.append(i)
            amicable.append(c)
            numbers.remove(c)


print(sum(set(amicable)))
