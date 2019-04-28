listi = []
for a in range(2,101):
    for b in range(2,101):
        listi.append(a**b)
listi.sort()
print(len(set(listi)))