n = int(input())
a = int(input())
save_n = n

k = 0

while n > 0:
    k += 1
    n = n//10
save_n += a * (10**k)
print(save_n)