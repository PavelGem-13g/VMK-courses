file = open("26-j1.txt ")
import math
n = int(file.readline())#int(input())int(file.readline())


d = {}

for i in range(1,100):
    d[i] = 0

for i in range(n):
    d[int(file.readline())]+=1

k = 0

for i in range(1,50):
    k += min(d[i],d[100-i])
k+=d[50]//2

print(k)
