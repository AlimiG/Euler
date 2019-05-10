import time
start = time.time()
def proper_divisors(n):
        numberofdivisors = 0
        i = 1
        while i <= n**0.5 + 1:
                if n%i == 0:
                        numberofdivisors +=1
                i+=1

        return numberofdivisors * 2 

print(proper_divisors(30))
triangular = []
"""
for i in range(1,100000):
    a = 0
    triangular.append(sum(list(range(1,i))))

j = 0
number = 0
while number <=500:
        n = triangular[j]
        number = proper_divisors(n)
        j +=1

print(triangular[j])"""

print(time.time()-start)