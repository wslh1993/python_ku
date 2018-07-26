import re
'''
with open('C:\\Users\\wslh1\\Desktop\\a.txt','r')as f:
    a=f.read()
p=re.compile(r'[a-z0-9A-Z]+\.[a-z0-9A-Z]+\.com')
data=p.finditer(a)
b=[]
for x in data:
    b.append(x.group())
    c=list(set(b))
print(c)

with open('C:\\Users\\wslh1\\Desktop\\a.txt','r')as f:
    a=f.read()
p=re.compile(r'<a\shref=.*>')
data=p.finditer(a)
for x in data:
    print(x.group())

'''
p = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
f = open('a.txt','r',encoding='utf8')
a = f.read()
print('\n'.join(p.findall(a)))
