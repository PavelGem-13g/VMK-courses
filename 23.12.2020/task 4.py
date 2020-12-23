n = int(input())
result = 0

while n>0:
    temp = n%10
    result = temp +result*10
    n//=10

print(result)