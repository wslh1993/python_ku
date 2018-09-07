""""
代码主要功能描述：实现英文和汉字的录入功能，
                  支持通过汉字查找英文、
                  支持通过英文查找汉字
				  支持词库遍历显示
                  支持精确拦截非法英文或汉字入库
编写人：李江锁
编写日期：2018-05-14 17:47， 修改次数3
程序版本：V1.2(修复了1.1版本中检测单词或汉字输入时，如果英文混有汉语出现成功入库的bug)
"""
dt={}#定义词库，存放汉字与英文对照表，英文为键，汉字为值
def input_basic_check(info):#实现输入功能，并初步对输入内容进行合法性检测，不合法则进行重新输入
    while True:
        temp=input(info)
        if temp != "" and temp.isalpha():  # 过滤掉输入的空字符串和非字母汉字类型
            return temp
        else:
            print("！警告：输入的字符串不是英文或者汉字，请重新输入")
def check_input_type(temp,state):#state=0则检测输入的类型为英文单词，检测合法返回真，如果state=1则检测输入的是类型是汉字，成功返回真
    lst=[]#存储传入字符串对应的字符编码
    if state==0:#检测英文
        for i in temp:
            lst.append(ord(i))#把传入的字符串逐个获取其编码，然后放入列表
        temp=max(lst)#找最大的编码如果是最大的也是小于255，则说明没有混有汉字
        if temp<255:
            return True
        else:
            return  False
    if state == 1:  # 检测中文
        for i in temp:
            lst.append(ord(i))
        temp = min(lst)#找最小的编码如果是最小的是小于255，则说明字符串里混有汉字
        if temp < 255:
            return False
        else:
            return True

def input_yh(en,ch):#负责接收输入的汉字和英语
    if check_input_type(en ,0) and check_input_type(ch,1):#入库前检测输入的单词和汉字是否有混合情况
         for i in dt:
             if i==en:#对输入的单词与库中存储单词做比对，如果出现重复则发出警告并取消存储。
                 print("！警告，库中存在该单词，请重新输入！")
                 break
         else:#没有执行break则说明没有重复则可以进行正常存储。
            dt[en] = ch
            print("存储成功！")
    else:
        print("！提示：输入的字符类型错误，存储失败！！！")

def find_ch(en):#英找汉函数
    if len(dt):#如果库里不为空才能进行查找操作
        for i in dt:
            if en==i:
                print(i+"对应的中文为>>>"+dt[i])
                break
        else:
            print("！-提示，你输入的英文在库中不存在！")
    else:
        print("！亲、词库为空，请开开开始你的学习吧！！！")

def find_en(ch):#汉找英实现函数
    if len(dt):
        for i in dt.items():
            if i[1]==ch:#利用i为元祖进行比对
                print(ch+"该汉字对应的英文为>>>："+i[0])
                break
        else:
            print("！-提示，没有该汉字对应的英文！！！")
    else:
        print("！亲、词库为空，请快开始你的学习吧！！！")
		
def show_all():#显示所有录入的英文单词及对应汉语
    if len(dt):
        for i in dt.items():
            print(i)
    else:
        print("词库为空")

print("*********欢迎使用XXX公司的单词学习系统V1.1***********")
while True:
    #菜单项显示
    opt=input("录入单词请输：  1\n"
              "英语查汉字请输：2\n"
              "汉字查英语请输：3\n"
              "退出系统请输：  4\n"
			  "查看所有输入all\n"
              "备注：停止录入输ex[当前收录*%s*条])\n"
              "请选择功能项："%len(dt))#动态显示成功入库的记录条数
    if opt=="1": #录入功能入口
        record_count=0
        while True:
            if len(dt)>record_count:#成功学习单词后显示鼓励信息
                record_count=len(dt)
                print("加油哦！亲，你已经学习%s个单词"%len(dt))
            en=input_basic_check("[录入单词]请输入英文：>>>")
            if en=="ex":#输入ex退出
                break
            ch=input_basic_check("[录入单词]请输入对应汉字:>>>")
            if ch=="ex":
                break
            input_yh(en, ch)#合法字符进行入库保存
    elif opt=="2":#英查汉功能入口
        en = input_basic_check("[英查汉]请输入英文:>>>")
        if check_input_type(en,0):
            find_ch(en)
        else:
            print("！-警告，你输入的不是英文")
    elif opt=="3":
        #ch = input(")
        ch= input_basic_check("[汉查英]请输入对应汉字:>>>")
        if check_input_type(ch,1):
            find_en(ch)
        else:
            print("！-警告你输入的不是汉字！")
    elif opt=="4":
        print("退出成功!")
        break
    elif opt=="all":
        show_all()
    else:
        print("！-警告，你输入的选项不存在，请重新输入！！！")
print("程序运行结束！")
