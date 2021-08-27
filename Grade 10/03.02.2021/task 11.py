n = int(input())
a = int(input())
d = int(input())
array = list()

for i in range(0,n):
    array.append(a + d*i)

print(array)