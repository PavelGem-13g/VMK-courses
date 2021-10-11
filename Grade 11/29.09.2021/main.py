def convert(a,base):
    alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    s = ''
    while a>0:
        s = alphabet[a%base]+s
        a//=base
    return s

print(convert(49**15+7**30-49,7).count('6'))
