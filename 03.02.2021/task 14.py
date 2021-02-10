n = int(input())
k = int(input())
array = list()

for i in range(0,n + 1):
    for j in range(0,i):
        array.append(k + i - 1)

print(array)