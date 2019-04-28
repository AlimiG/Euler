def champer(last):
    answer = ""
    for c in range(last):
        answer += str(c)
    return answer

champ = champer(200000)
answer = 1
for c in range(6):
    answer*= int(champ[10**c])
print(answer)