file = open("26-J1.txt")
import math
n = int(file.readline())#int(input())int(file.readline())

l = list()

d = {}

for i in range(1,100):
    d[i] = 0

for i in range(n):
    l.append(int(file.readline()))
    
for i in l:
    d[i]+=1


k = 0

for i in range(1,50):
    k += min(l[i],l[100-i])

k+=l[50]//2

print(k)
