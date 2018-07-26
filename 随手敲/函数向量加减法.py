
def sump(*a):
    s=0
    for x in a:
        if len(x)>s:
            s=len(x)
    for x in a:
        s1=s-len(x)
        a.extend([int(x)for x in '0'*s1])
    s=[]
    for x in zip(*a):
        s.append(sum(x))
    return s


def sub(a,b):
    if len(a)>len(b):
        s=len(a)
    else:
        s=len(b)
    for x in (a,b):
        print(x)
        if s>len(x):
            x.extend([int(x)for x in '0'*s])
    s=[]
    for x,y in zip(a,b):
        s.append(x-y)
    return s

def dot(a,b):
    s=0
    for x,y in zip(a,b):
        s+=x*y
    return s

def xc(a,b):
    s=[]
    for x in a:
        a=[]
        for y in b:
            a.append(x*y)
        s.append(a)
    return s

