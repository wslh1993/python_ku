'''
def sn(**a):
        while True:
            suc=input('请输入姓名')
            suc=suc.strip()
            if suc=='退出':
                break
            opt=a.get(suc,404)
            if  opt==404:
                opt=input('输入身高')
                a[suc]=opt.strip()
        print(a)
        s=0
        for i in a.values():
                s=s+int(i)
        g=s/len(a)
        print('平均身高%d总身高%d'%(g,s))
        return g

d={}
while True:
    suc=input('请输入姓名')
    suc=suc.strip()
    if suc=='退出':
        break
    opt=d.get(suc,404)
    if  opt==404:
        opt=input('输入身高')
        d[suc]=opt.strip()

a={}
sn(**a)
'''
def sg(*z):
        return sum(z)/len(z)

def sx(**l):
        for x,y in l.items():
                print(x,y)

