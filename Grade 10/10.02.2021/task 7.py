n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

flag = True

for i in range(0,n):
    if array[i]>0:
        flag = False
    if flag and array[i]<0:
        array[i] = 0

print(array)