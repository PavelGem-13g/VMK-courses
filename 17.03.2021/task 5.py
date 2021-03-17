import string
s=input()
sreversed = ''.join(reversed(s))
if s==sreversed:
    print('Yes')
else:
    print('No')