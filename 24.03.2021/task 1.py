def is_thriple_del(a):
    deli = -1
    deli2 = 0
    k = 0
    for i in range(2, a // 2 + a % 2+1):
        if a % i == 0:
            deli2 = deli
            deli = i
            k+=1
    if k==3:
        return deli2
    return -1

dictionary = dict()
for i in range(10, 10000):
    temp = is_thriple_del(i)
    if temp != -1:
        dictionary[i] = temp
        print(temp,i)
