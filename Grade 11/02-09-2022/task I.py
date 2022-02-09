a = int(input())
b = int(input())
c = int(input())

chet = False
if a%2==0:
    chet = True
if b%2==0 and not chet:
    chet = True
if c%2==0 and not chet:
    chet = True

nechet = False
if a%2!=0:
    nechet = True
if b%2!=0 and not nechet:
    nechet = True
if c%2!=0 and not nechet:
    nechet = True

if chet and nechet:
    print('YES')
else:
    print('NO')