n = int(input())
a = int(input())

k = 0

while n > 0:
    k += 1
    n = n//10
print(a * (10**k))
n += a * (10**k)
print(n)