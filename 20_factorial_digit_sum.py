a = 1
for i in range(1,101):
    a = a*i

sum = 0
for j in str(a):
    sum = sum + int(j)

print(sum)