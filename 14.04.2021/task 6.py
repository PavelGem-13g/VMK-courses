def f(n,count):
    count+=1
    if count>1000:
        return 0
    if n<=1:
        return 1
    elif n>1 and n%2==0:
        return 3+f(n//2-1,count)
    elif n>5 and n%2!=0:
        return n+f(n+2,count)
    return 0


for i in range(1,1000):
    if f(i,0) == 19:
        print(i)
        break
       
