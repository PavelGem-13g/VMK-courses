isZero = False
n = int(input())
new_n = 0
k = 0

while n > 0:
    temp = n % 10
    new_n+=10**k*temp
    k+=2
    n //= 10
print(new_n)
