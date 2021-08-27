file = open("26-1.txt")

s,n = map(int, file.readline().split())
l = list()

for i in range(n):
    l.append(int(file.readline()))

l = sorted(l)

maxs = 0
k = 0
flag = False

for i in l:
    if s-i>0:
        s-=i
        k+=1
        maxs = i
    if s-i==0:
        maxs = i
        s-=i
        k+=1
        flag = True

if not flag:
    s+=maxs
    for i in l:
        if s-i>=0:
            maxs = i

print(k,maxs)
