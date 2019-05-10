with open('number.txt','r') as f:
    data = f.read()
listy = []
summ = '0'
for i in data:
    if i != '\n':
        summ = summ + i
    else:
        listy.append(int(summ))
        summ = '0'

print(sum(listy))