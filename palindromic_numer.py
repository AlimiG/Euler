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

biggest = 0
for i in range(100,999):
    for j in range(100,999):
        if checkpalindromic(i*j) == True:
            if (i*j) > biggest:
                biggest = i*j

print(biggest)
