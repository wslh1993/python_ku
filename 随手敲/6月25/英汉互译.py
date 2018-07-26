import logging
logging.basicConfig(level=logging.INFO,filename='myapp.log')
d={}#定义空字典
while True:#无限循环
    suc=input('请输入内容')#输入内容放进suc(键)
    suc=suc.strip()#去空格
    logging.info('suc = %s' % suc) 
    if suc=='88':#判断条件等于88
        print('退出')#输出退出
        break
    opt=d.get(suc,404)#键suc的 值opt为 404
    logging.info('opt = %s' % opt) 
    for x in d.items():#把d 变成('key','value') 
        if suc in x and suc in d.keys():#如果suc在键里 
            opt=x[1]#value赋给opt
            logging.info('opt = %s' % opt)
        elif suc in x:#否则 suc在 值里
            opt=x[0]#把name赋给opt
            logging.info('opt = %s' % opt)
    if  opt==404:#判断opt等于404
        opt=input('字典未收录，请输入翻译')#输入一个值赋给opt
        d[suc]=opt.strip()#把去空格的opt赋给字典d的key的value
        logging.info('d = %s' % d)
    else:#不等于404
        print('翻译结果:%s'%(opt,))#输出opt的值
'''
输入内容
（设置退出功能）
给值赋404
判断字典是否收录
（遍历d 判断输入内容是键还是值，赋值给opt 输出翻译）
没有收录
输入翻译
收录
输出翻译

'''
