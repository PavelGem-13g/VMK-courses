n = int(input())
result = 0
for i in range(0, n):
    temp = int(input())
    if temp==1:
        result += 2** (n-i-1)
print(result)