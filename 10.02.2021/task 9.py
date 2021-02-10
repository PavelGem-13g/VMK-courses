n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

_max = 0
_maxi = 0

for i in range(0,n):
    if _max<array[i]:
        _max = array[i]
        _maxi = i

temp = array[_maxi]
array[_maxi] = array[0]
array[0] = temp

print(array)