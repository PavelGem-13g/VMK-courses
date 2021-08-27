import random
n = int(input())

arr = []

for i in range(n):
    arr.append([0]*n)

for j in range(0,n):
    summa = 0
    for i in range(0,n):
        arr[i][j] = random.randint(0,20)

summa = 0
flag = False

for i in range(len(arr[0])):
    summa += arr[0][i]

for i in range(len(arr)):
    summ = 0
    for j in range(len(arr[i])):  
        summ += arr[i][j]
    if summ!=summa:
        flag = True
        break

for i in range(len(arr)):
    summ = 0
    for j in range(len(arr[i])):  
        summ += arr[j][i]
    if summ!=summa:
        flag = True
        break

if not flag:
    print('Yes')
else:
    print('No')
