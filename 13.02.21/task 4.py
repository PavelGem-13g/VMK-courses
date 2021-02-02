n = int(input())
_max = 0
_min = 10
n_copy = n
k = 0
while n_copy > 0:
    temp = n_copy % 10
    if temp >= _max:
        _max = temp
    if temp <= _min:
        _min = temp
    n_copy //= 10
    k += 1
result = 0
while k >= 0:
    temp = (n // (10**k)) % 10
    if temp == _min:
        temp = _max
    elif temp == _max:
        temp = _min
    result *= 10
    result += temp
    k-=1
print(result)