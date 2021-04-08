def f(a):
    if a==1:
        return 2
    if a==2:
        return 1
    if a>2:
        return 2*f(a-1)-f(a-2)

print(f(int(input())))