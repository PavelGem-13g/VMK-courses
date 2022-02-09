n = int(input())
if n % 5 == 0 or n % 5 % 3 == 0 or n % 3 == 0 or n % 3 % 5 == 0:
    print("YES")
else:
    print("NO")