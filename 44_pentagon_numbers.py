import time
start = time.time()
pentagonian_list = []
def pentagonian(n):
    if n not in pentagonian_list:
        pentagonian_list.append(int(n*(3*n-1)/2))
    return

for i in range(100000):
    pentagonian(i)

pairs = []
for i in range(len(pentagonian_list)):
    for j in range(len(pentagonian_list)):
        if i+j in pentagonian_list and i-j in pentagonian_list:
            pairs.append([i,j])


print(pairs)

print(time.time()-start)