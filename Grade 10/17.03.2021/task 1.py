import string
s=input()
d = dict.fromkeys(string.ascii_lowercase, 0)
a = ""
for i in d:
    if s.count(i)>0:
        a+=i+" "+str(s.count(i))+"\n"
print(a[0])