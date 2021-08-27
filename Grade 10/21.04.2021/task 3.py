import random
n = int(input())
m = int(input())

arr = []

for i in range(n):
    arr.append([0]*m)

for j in range(0,m):
    summa = 0
    for i in range(0,n):
        arr[i][j] = random.uniform(-1,20)

flag = False

for i in range(0,n):
    k = len(arr[i])
    for j in range(0,m):
        if arr[i][j]<0:
            k-=1
    if k == 0:
        flag = True
        break
    if flag:
        break

if flag:
    print('Yes')
else:
    print('No')
