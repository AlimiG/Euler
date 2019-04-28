result = 0
g = 1000
for i in range(g):
    if i%3 == 0 or i%5 == 0:
        result = result + i

print("Final\n")
print(result)