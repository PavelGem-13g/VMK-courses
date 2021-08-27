max6 = 0
max2 = 0
max3 = 0
maxi = 0

n = int(input())

for i in range(0, n):
    temp = int(input())

    if temp % 6 == 0 and temp > max6:
        max6 = temp
    elif temp > maxi:
        maxi = temp
    elif temp % 3 == 0 and temp > max3:
        max3 = temp
    elif temp % 2 == 0 and temp > max2:
        max2 = temp

R = 0
if max6==0:
    R = max2*max3
else:
    R = max6*maxi
print(max6,max3,max2,maxi)
print(R)
