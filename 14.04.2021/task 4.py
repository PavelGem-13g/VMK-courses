def f(n,count):
    count+=1
    if count>1000:
        return 0
    if n<=5:
        return n
    elif n>5 and n%8==0:
        return n+f(n//2-3,count)
    elif n>5 and n%8!=0:
        return n+f(n+4,count)


maxi = 0
for i in range(1,100001):
    if f(i,0)!= 0:
        maxi = i

print(maxi)        
