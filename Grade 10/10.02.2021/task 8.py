n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

temp = array[-1]
array[-1] = array[0]
array[0] = temp

print(array)