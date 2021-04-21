import random
n = int(input())
m = int(input())

arr = []

for i in range(n):
    arr.append([0]*m)

for j in range(0,m):
    summa = 0
    for i in range(0,n):
        arr[i][j] = random.randint(0,100)

for j in range(0,m):
    summa = 0
    for i in range(0,n):
        summa+=arr[i][j]
    if summa > 100:
        print(j)
