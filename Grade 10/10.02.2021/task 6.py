n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

flag = False

for i in range(0,n):
    if array[i]==0:
        flag = True
    if flag:
        array[i] = -array[i]

print(array)