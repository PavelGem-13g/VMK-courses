file = open('26.txt')

s,n = map(int,file.readline().split())

l = []

for i in range(n):
    l.append(int(file.readline()))

l = sorted(l)

k = 0
maxm = 0
for i in l:
    if n-i>=0:
        k+=1
        n-=i
        maxm = i

n+=i
for i in l:
    if n-i>=0:
        maxm = i

print(k,maxm)