def proper_divisors(n):
    listi = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            listi.append(i)
            print(listi)
    return len(listi)


print(proper_divisors(28))
""""
triangular = []
for i in range(1,20000+1):
    a = 0
    triangular.append(sum(list(range(1,i))))

print(len(triangular))

for i in triangular:
    z = proper_divisors(i)
    if z == 500:
        print(i)
      break

"""