n = int(input())
number = int(input())

length = 0
temp_n = n
while temp_n >0:
    temp_n //=10
    length += 1

result = 0

if length-number>=0:
    result = n // pow(10,length-number)
    result %= 10
print(result)
