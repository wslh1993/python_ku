d={}
while True:
    suc=input('请输入内容')
    suc=suc.strip()
    if suc=='88':
        print('退出')
        break
    opt=d.get(suc,404)
    if  opt==404:
        opt=input('输入内容')
        d[suc]=opt.strip()
    else:
        print('结果:%s'%(opt,))
'''
输入内容
去空格
（设置退出功能）
值为空
判断字典是否收录
没有收录
输入翻译
收录把值赋给键

循环重新开始
 输入之前输过的内容
 两个if都不符合
 输出翻译
'''
