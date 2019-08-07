import time
start = time.time()

s,x,y = 0,0,2 
limit = 4000000
while y < limit:
    x,y,s = y,4*y+x,s+y

print(s)
print(time.time()-start)