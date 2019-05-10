def dec_to_bin(n):
    return int(bin(n)[2:])

def checkpalindromic(num):
    temp = num
    rev = 0
    while( temp != 0):
        rev = (rev*10)+(temp%10)
        temp = temp //10

    if num == rev:
        return True
    else:
        return False
listy = []
summ = 0
for i in range(1,1000000,2):
    if checkpalindromic(i) and checkpalindromic(dec_to_bin(i)):
        listy.append(i)

print(listy, sum(listy))