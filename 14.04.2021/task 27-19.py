file = open('27-19a.txt')

s = 1
sm = 0
n = int(file.readline())
temp = 0
km = 0
for i in range(0,n):
    temp = int(file.readline())
    if temp!=0:
        s *= temp
    elif temp==0:
        if sm < s:
            sm = s
            s = 0

print(sm)
file.close();
