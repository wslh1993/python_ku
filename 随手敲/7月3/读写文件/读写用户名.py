while True:
    a=input('输入用户名')
    if a=='88':
        break
    b=input('输入密码')
    with open('C:\\Users\\wslh1\\Desktop\\用户.txt','a')as f:
        f.write('用户名:%s密码:%s\n'%(a,b))
        f.close()

with open('C:\\Users\\wslh1\\Desktop\\用户.txt','r')as f:
    for x in f.readlines():
        print(x)
