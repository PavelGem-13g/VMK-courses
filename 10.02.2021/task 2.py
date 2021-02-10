n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

for i in range(n-1,0,-1):
    if array[i-1]%2==0:
        array[i]=0

print(array)