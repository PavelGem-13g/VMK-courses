n = int(input())
flag = False

for i in range(n):
    if int(input())==0:
        flag = True

if flag:
    print('YES')
else:
    print('NO')