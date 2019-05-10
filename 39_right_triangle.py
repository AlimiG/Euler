import time
start = time.time()
list720 = [[270, 144, 306], [288, 120, 312], [315, 80, 325], [320, 72, 328], [288, 120, 312], [270, 144, 306], [320, 72, 328]]
list960 = [[315, 168, 357], [336, 140, 364], [252, 240, 348], [350, 120, 370], [252, 240, 348], [390, 56, 394], [399, 40, 401]]
list840 = [[360, 192, 408], [384, 160, 416], [320, 240, 400], [360, 192, 408], [384, 160, 416], [448, 60, 452], [384, 160, 416]]
"""solutions = {}
for i in range(300):
    for j in range(100):
        for k in range(1,500):
            a = k*((i**2)-(j**2))
            b = 2*i*j*k
            c = ((i**2)+(j**2))*k
            if a > 0 and b > 0 and c > 0 and a > b:
                if a+b+c <=1000:
                    if (a + b + c) in solutions:
                        solutions.update({a+b+c : solutions[a+b+c]+1})
                        if(a+b+c) == 960:
                            list960.append([a,b,c])
                        if(a+b+c) == 840:
                            list840.append([a,b,c])
                        if(a+b+c) == 720:
                            list720.append([a,b,c])
                    else:
                        solutions.update({a+b+c : 1 })


print(max(solutions, key = solutions.get))"""
list720.sort()
list840.sort()
list960.sort()
print(list720)
print(list840)
print(list960)
print(time.time()-start)