import time
start = time.time()
print(len(str(3508)))
def createfibo(n):
    fib = [1,1]
    for i in range(1,n):
        fib.append(fib[i]+fib[i-1])
    return fib

fib = createfibo(10000)
for i in fib:
    if len(str(i)) == 3:
        print(fib.index(i)+1)
        break


print(time.time() - start)