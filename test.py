def numberOfDivisors(a):
    m=0
    for j in range(1,a/2+1):
        if (a%j)==0:
            m+=1
    return m+1

def findNumber():
    n = 1
    i = 1
    div = numberOfDivisors(n)
    while div < 500:
        i += 1        
        n = i*(i+1)/2
        div = numberOfDivisors(n)
        print ('n = ', n)
    return n

findNumber()