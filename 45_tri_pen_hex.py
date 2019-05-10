listy = []
for i in range(1,50000):
        a = i*(i+1)
        for y in range(1,50000):
                b = y*(3*y-1)
                for z in range(1,50000):
                        c = 2*z*(2*z-1)
                        if a == b and c==a:
                                listy.append(i)
                

print(listy)