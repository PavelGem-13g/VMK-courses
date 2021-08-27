n = int(input())
new_n = 0

while n > 0:
    temp = n % 10
    if temp % 2 == 0:
        new_n = new_n * 10 + temp
    n = n // 10
print(new_n)