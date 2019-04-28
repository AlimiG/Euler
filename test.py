import math
a = 0
for i in range(1,20000000):
    a = a + 1/(i*i)
print(math.sqrt(6*a))