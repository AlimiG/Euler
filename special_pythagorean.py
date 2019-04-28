a = b = c = 0

for m in range(0,100):
    for n in range(0,100):
        a = (m**2)-(n**2)
        b = 2*m*n
        c = (m**2)+(n**2)
        if (a+b+c) == 1000:
            print(a*b*c)
