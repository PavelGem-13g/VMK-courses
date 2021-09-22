def f(n):
    if n==1:
        return 5
    if n%2==0:
        return 2*n+f(n-1)
    if n%2!=0 and n >1:
        return 3*f(n-2)+f(n-1)

print(f(35))