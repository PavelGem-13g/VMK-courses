file = open('27-8b.txt')
n = int(file.readline())
l = list()
for i in range(0,n):
    l.append(int(file.readline()))

min = sorted(l)[-1]**2+sorted(l)[-2]**2
for i in range(0,len(l)-5):
    if (l[i]**2+l[i+5]**2)<min:
        min = l[i]**2+l[i+5]**2
print(min)  