p = 1
res = 1
N = int(input())
for i in range(N, 0, -1):
    p *= i
    res += p
res /= p
print(res)
