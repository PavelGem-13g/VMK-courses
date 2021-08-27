file = open("27-11b.txt")
n = int(file.readline())
summ = 0

delta = dict()
for i in range(0,8):
    delta[i] = 10000

for i in range(0,n):
    l = list(map(int, file.readline().split()))
    summ += max(l)
    for i in l:
        if i!=max(l)and delta[(max(l)-i)%8]>max(l)-i:
            delta[(max(l)-i)%8] += max(l)-i
            
for i in range(0,len(delta)):
    if (summ-i)%8==0:
        summ-=i
    
print(summ)
    
