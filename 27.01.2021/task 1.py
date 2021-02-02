n = int(input())
temp1 = int(input())
k = 0
for i in range(0, n - 1):
    temp2 = int(input())
    if temp2 > temp1:
        k += 1
    temp1 = temp2
print(k + 1)
