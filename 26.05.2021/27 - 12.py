file = open('27-12a.txt')

n = int(file.readline())

l = list()
for i in range(n):
    l.append(int(file.readline()))

k_6 = 0
k_2 = 0
k_3 = 0
k_0 = 0
s = 0
for i in l:
    if i%6!= 0:
        k_0 += 1
    if i%2==0:
        k_2 +=1
    if i%3==0:
        k_3 +=1    
    if i %6== 0:
        s+=k_0
        k_6 += 1

s += min(k_2,k_3)*2
print(s)
