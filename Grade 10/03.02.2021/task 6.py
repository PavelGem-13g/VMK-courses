n = int(input())
array = list()

if n%2==0:
    array.append(n)
    n-=1

for i in range(0, n, 2):
    array.append(n - i)

print(array)