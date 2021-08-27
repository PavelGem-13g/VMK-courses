n = int(input())
temp1 = int(input())
temp_repeat = 0
result = ""
for i in range(0, n - 1):
    temp2 = int(input())
    if temp2 == temp1:
        temp_repeat += 1
    if temp2 > temp1:
        result += str(temp1) + ' ' + str(temp_repeat + 1)+ '\n'
        temp_repeat = 0
    temp1 = temp2
result += str(temp1) + ' ' + str(temp_repeat + 1) + '\n'
print(result)