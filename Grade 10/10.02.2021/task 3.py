def find3(a):
    delta = 0
    if (a + delta)%3==0:
        return a+delta
    if (a - delta) % 3 == 0:
        return a - delta
    delta+=1
    return find3(a+delta)

n = int(input())
array = list()

for i in range(0,n):
    array.append(int(input()))

for i in range(0,n):
    if array[i]%3!=0:
        array[i] = find3(array[i])

print(array)
