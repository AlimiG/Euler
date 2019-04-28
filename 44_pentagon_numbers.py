pents = []
for k in range(1000):
    listi = []
    for x in range(1000):
        for y in range(1000):
            if (6*(k**2)-1) == ((6*(x**2)-1)+(6*(y**2)-1)):
                listi.append((6*(k**2)-1),(6*(x**2)-1),(6*(y**2)-1))
pents.append(listi)

print(pents)