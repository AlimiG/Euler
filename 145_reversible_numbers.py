def reverse(num):
    temp = num
    rev = 0
    while( temp != 0):
        rev = (rev*10)+(temp%10)
        temp = temp //10
    return rev

def checkeo(num):
    for i in range(len(str(num))):
        if int(str(num)[i]) % 2 == 0 :
            return False
    return True



print(str(reverse(10)))
listofreversible= []
for i in range(1,1000000000):
    if i % 10 != 0 :
        if checkeo(i+reverse(i)):
            listofreversible.append(i)


print(len(listofreversible))