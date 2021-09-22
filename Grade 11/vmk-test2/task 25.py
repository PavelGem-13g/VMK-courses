import math

def find_del(a):
    for i in range(2,int(math.sqrt(a))):
        if a%i==0:
            return i+a//i
    return 0

k = 0

i = 1234569345
while k!=3:
    temp = find_del(i)
    if temp%1000==118:
        print(i,temp)
        k+=1
    i+=1