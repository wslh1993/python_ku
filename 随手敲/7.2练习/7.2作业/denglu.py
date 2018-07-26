user={'张三':'123456'}
n=0
while n<3:
    name=input('输入用户名:')
    pwd=input('输入密码:')
    try:
        if user[name]==pwd:
            print('登陆成功')
            break
        else:
            print('ERROR')
            n+=1
    except KeyError:
        print('用户名错误')
        n+=1
else:
    print('ERROR大于三次')
    
'''
输入用户名密码
判断输入与预设相等
不等报错 
相等 登陆成功
错误大于三次跳出
'''
