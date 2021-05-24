file = open('27-10b.txt')
n = int(file.readline())
summ = 0
mind = 10000

for i in range(0,n):
    l = list(map(int, file.readline().split()))
    summ += max(l)
    del l[l.index(min(l))]
    if (max(l) - min(l))<mind and (max(l) - min(l))!=0:
        mind = max(l) - min(l)

if summ%4==0:
    summ-=mind
print(summ)
    
