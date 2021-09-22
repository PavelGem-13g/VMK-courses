file = open('24.txt')

s = file.read()

l = 0
maxl = 0
for i in range(len(s)-1):
    if s[i] == 'S' and s[i+1]=='Q':
        if maxl<l:
            maxl = l
        l = 0
    else:
        l+=1

print(maxl+1)