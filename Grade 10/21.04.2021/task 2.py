import random
n = int(input())
m = int(input())

arr = []

for i in range(n):
    arr.append([0]*m)

for j in range(0,m):
    summa = 0
    for i in range(0,n):
        arr[i][j] = random.randint(0,3)

print('столбцы')
for j in range(0,m):
    k = 0
    for i in range(0,n):
        if arr[i][j]==1:
            k+=1
    if k == 1:
        print(j)

print('строки')

for i in range(0,n):
    k = 0
    for j in range(0,m):
        if arr[i][j]==1:
            k+=1
    if k == 1:
        print(i)
