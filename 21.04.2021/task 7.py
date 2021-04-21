import random
n = int(input())

arr = []

for i in range(n):
    arr.append([0]*n)

for j in range(0,n):
    summa = 0
    for i in range(0,n):
        arr[i][j] = random.randint(0,20)

arr = sorted(arr, key = lambda x:sum(x))

for i in range(len(arr)):         
    for j in range(len(arr[i])):  
        print(arr[i][j], end = '\t')
    print()  
