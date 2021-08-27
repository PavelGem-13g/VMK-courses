file = open("26-k2.txt")

n,k = map(int, file.readline().split())
l = list()

for i in range(n):
    l.append(int(file.readline()))

l = sorted(l)
for i in range(k):
    del l[0]
    del l[len(l)-1]

print(max(l),int(sum(l)/len(l)))
