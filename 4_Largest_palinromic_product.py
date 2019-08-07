def is_palindromic(n): n=str(n); return n==n[::-1]

pmax, L = 0,1000000
for i in range(999,100,-1):
    for j in range(990,100,(-11 if i%1 else -1)):
        p = i*j
        if p < pmax: break
        if p < L and is_palindromic(p): x,y, pmax = i,j,p

print(pmax)