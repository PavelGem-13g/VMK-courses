file = open("26-k1.txt")

n,k = map(int, file.readline().split())
l = list()

for i in range(n):
    l.append(int(file.readline()))

l = sorted(l,reverse = True)

maxs = l[k]

summ = 0

for i in range(k):
    summ+=0.2*l[i]

print(maxs,summ)
