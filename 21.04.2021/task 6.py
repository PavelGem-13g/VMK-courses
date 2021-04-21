import random
n = int(input())

arr = []

for i in range(n):
    arr.append([0]*n)

for j in range(0,n):
    summa = 0
    for i in range(0,n):
        arr[i][j] = random.randint(0,0)

flag = False

for i in range(len(arr)):
    for j in range(len(arr)):  
        if i!=j and arr[i]==arr[j]:
            print(arr[i],arr[j])
            flag = True
            break
            
for i in range(len(arr)):
    l = []
    jk = 0
    for jk in range(len(arr[i])):  
        l.append(arr[i][jk])
    l1 = []
    for j in range(len(arr[i])):  
        l1.append(arr[i][j])
        if jk!=j and  l==l1:
            flag = True
            break

if flag:
    print('Yes')
else:
    print('No')
