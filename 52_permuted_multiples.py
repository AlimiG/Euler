import time
start = time.time()
def check(n):
    flag = True
    for i in range(1,6):
        a = list(str(n*i))
        b = list(str(n*(i+1)))
        a.sort()
        b.sort()
        if a == b:
            flag = flag and True
        else:
            return False
    return flag
    
list2 = []
"""
for i in range(1,5000000):
    if check(i) :
        list2.append(i)

"""
list2.sort()
print(check(30))

print(time.time()-start)

