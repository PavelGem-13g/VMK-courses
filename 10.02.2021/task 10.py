n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

_max = 0
_maxi = 0

_min = 10
_mini = 0

for i in range(0,n):
    if _max < array[i]:
        _max = array[i]
        _maxi = i

    if _min > array[i]:
        _min = array[i]
        _mini = i

temp = array[_maxi]
array[_maxi] = array[_mini]
array[_mini] = temp

print(array)