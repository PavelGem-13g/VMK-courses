def is_delta_10(array):
    f = 0
    for i in range(0,len(array)-1):
        if array[i]+10 == array[i+1]:
            f+=1
    return f+1==len(array)

def find_del(a):
    dels = list()
    k = 0
    for i in range(2, a // 2 + a % 2 + 1):
        if a % i == 0:
            dels.append(i)
            k += 1
    if is_delta_10(dels) and k>1:
        return dels
    return -1


for i in range(10, 1000):
    temp = find_del(i)
    if temp != -1:
        print(temp, i)
