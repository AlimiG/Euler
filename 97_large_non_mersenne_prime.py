import time
start = time.time()
n = 2
for i in range(7830456): n = (n*2)%10000000000
n = n*28433 +1  
print(str(n)[-10:])
print(time.time()-start)