def input_num():
    while True:
        num=input('请输入数字')
        try:
            num=int(num)
            break
        except ValueError:
            try:
                num=float(num)
                break
            except:
                print('you input error')
            return num
        except:
            print('error')
a=input_num()
b=input_num()
print(a+b)
'''
输入数字
判断是是否整型和浮点型
是 运算
不是 输出‘你的输入有误’
'''
