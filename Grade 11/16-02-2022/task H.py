def factorial(a):
    s = 1
    for i in range(1,a+1):
        s*=i
    return s

n = int(input())
k = int(input())
result = (factorial(n))/(factorial(k)*factorial(n-k))
print(int(result))