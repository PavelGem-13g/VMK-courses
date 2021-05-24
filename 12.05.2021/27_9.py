from array import *
file = open('27-9b.txt')

n = int(file.readline())

l = array('i',[0,0,0,0,0,0])

mini = 100000
minp = 100000

for i in range(0,6):
    l[i] = int(file.readline())

for i in range(6,n-1):
    temp = int(file.readline())
    if l[0]%2!=0 and l[0]<mini:
        mini = l[0]
    if temp%2!=0 and temp*mini < minp:
        minp = temp*mini
    del l[0]
    l.append(temp)
    
print(minp)
