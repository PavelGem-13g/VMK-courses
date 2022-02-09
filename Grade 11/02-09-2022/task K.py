a,b = map(int,input().split())
if a==21:
    print('Vasya wins')
elif b==21:
    print('Petya wins')
if 0<(a+b)%10<5:
    print('Vasya serves')
else:
    print('Petya serves')
