n = int(input())
temp1 = int(input())
temp2 = 0
result = ""
for i in range(0, n - 1):
    temp2 = int(input())
    if temp2 >= temp1:
        result += str(temp1) + ' '
    else:
        result += str(temp1) + '\n'
    temp1 = temp2
result += str(temp1) + '\n'
print(result)
