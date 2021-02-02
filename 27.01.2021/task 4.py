n = int(input())
temp1 = int(input())
temp2 = 0
k = 0
max_k = 0
for i in range(0, n - 1):
    temp2 = int(input())
    if temp2 < temp1:
        k += 1
    else:
        if max_k<k:
            max_k = k
        k = 0
    temp1 = temp2
if max_k < k:
    max_k = k
print(max_k + 1)
