file = open('17.txt')

s = file.read()

l = s.split()

for i in range(len(l)):
    l[i] = int(l[i])

k = 0
maxs = 0
for i in range(len(l)-1):
    if l[i]%5==0 or l[i+1]%5==0:
        k+=1
        if maxs < l[i]+l[i+1]:
            maxs = l[i]+l[i+1]

print(k,maxs)