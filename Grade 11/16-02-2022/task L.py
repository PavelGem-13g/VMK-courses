n = int(input())

k = 0
for i in range(n+1):
    for j in range(i):
        if k<n:
            print(i,end=' ')
            k+=1