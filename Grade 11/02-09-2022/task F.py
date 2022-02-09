a = int(input())
b = int(input())
c = int(input())

d = int((b*b-4*a*c)**1/2)
if d==0:
    print(-b//(2*a))
elif d>0:
    print((-b-d)//(2*a))
    print((-b+d)//(2*a))
