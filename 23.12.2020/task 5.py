n = int(input())
a = int(input())
result = 0

while n > 0:
    temp = n % 10
    if temp != a:
        result = temp + result * 10
    n //= 10

n = result
new_result = 0

while n > 0:
    temp = n % 10
    new_result = temp + new_result * 10
    n //= 10

print(new_result)