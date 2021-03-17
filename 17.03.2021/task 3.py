import string
s=input()
d = dict.fromkeys(string.ascii_lowercase, 0)
dictionary = dict()
for i in d:
    if s.count(i)>0:
        dictionary[i] = s.count(i)
print(sorted(dictionary,key=dictionary.get,reverse=True))