n = int(input())
array = list()

array.append(1)
array.append(1)

for i in range(2,n):
    array.append(array[i-1] + array[i-2])

print(array)