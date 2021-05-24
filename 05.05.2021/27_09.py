file = open("27-9b.txt")

n = int(file.readline())

l = list()
mintop = 0
mini = 100000
for i in range(6):
    temp = int(file.readline())
    if temp%2==1:
        mintop = min(temp,mintop)

for i in range(6,n):
    temp = int(file.readline())
    if mini>=temp*mintop and temp%2==1:
        mini = temp*mintop
        mintop = min(temp,mintop)

print(mini)
