

def del_count(k):
    result = 0
    for i in range(0,k):
        if n % i:
            result+=1
    return  result
n = int(input())
for i in range(0,n + 1):
    if i<3:
        print(i)