a=int(input())
lirun=[1000000,600000,400000,200000,100000,0]
jiang=[0.01,0.015,0.03,0.05,0.075,0.1]
j=0
for i in range(0,6):
    if a>lirun[i]:#判断输入的利润大于多少
        j=j+(a-lirun[i])*jiang[i]#各个档位累加奖金（总奖金）
        print((a-lirun[i])*jiang[i])#输出每个档位的奖金
        a=lirun[i]#下面的档位剩余的利润
        print('--------------')#分隔符
        print(a)#输出下面档位剩余利润
print(j)#输出总奖金
