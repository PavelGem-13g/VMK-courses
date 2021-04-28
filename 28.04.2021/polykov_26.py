file = open("26-J1.txt")
import math
n = int(file.readline())#int(input())int(file.readline())

l = list()

for i in range(n):
    l.append(int(file.readline()))#(int(file.readline()))

k = 0

for i in range(0,len(l)-1):
    for j in range(i,len(l)-1):
        if i!=j and l[i]+l[j]==100:
            k+=1
            if i<j:
                del l[j]
                del l[i]
            else:
                del l[i]
                del l[j]
            break

print(k)
