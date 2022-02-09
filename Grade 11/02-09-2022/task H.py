n = int(input())
m = n % 100

if m <= 10 or m >= 20:
    if (n % 10) == 0 or ((n % 10) >= 5 and (n % 10) <= 9):
        print(str(n) + " bochek")
    elif (n % 10) == 1:
        print(str(n) + " bochka")
    else:
        print(str(n) + " bochki")
else:
    print(str(n) + " bochek")