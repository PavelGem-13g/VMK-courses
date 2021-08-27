def f(n,count):
    count+=1
    if count>1000:
        return 0
    if n<=5:
        return n
    elif n>5 and n%5==0:
        return n+f(n//5-1,count)
    elif n>5 and n%5!=0:
        return n+f(n+6,count)


for i in range(1,100001):
    if f(i,0) > 100:
        print(i)
        break
       
