for i in range(10):
    s='*'*10
    print(s.rjust(10+i))
for i in range(10):
    s='*'*i
    if i%2==1:
        print(s.center(13))
for i in range(8,0,-1):
    if i%2==1:
        s='*'*i
        print(s.center(13))
for i in range(1,10):#i控制行数
    for j in range(1,i+1):#j控制列数
        print('%d*%d=%d'%(j,i,i*j),end='\t')#末尾换行改成制表符\t
    print('\n')#一行加一个换行
for i in range(9,0,-1):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,i*j),end='\t')
    print('\n')
