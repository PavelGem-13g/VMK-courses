a = int(input())
b = int(input())
c = int(input())

if ((a*a) + (b*b)) == c*c or ((a*a) + (c*c)) == a*a or ((a*a) + (c*c)) == b*b or ((c*c) + (b*b)) == a*a:
    print('right')
if a + b > c or a + c > b or a + c > b or c + b > a:
    print('acute')
if a + b < c or a + c < b or a + c < b or c + b < a:
    print('obtuse')
else:
    print('impossible')