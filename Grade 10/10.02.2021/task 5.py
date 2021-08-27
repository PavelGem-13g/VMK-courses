n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

for i in range(2,n,3):
    array[i] = array[i-1] + array[i-2]

print(array)