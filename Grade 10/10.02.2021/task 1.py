n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

for i in range(0,n):
    if array[i]%2==0:
        array[i] = 0

print(array)