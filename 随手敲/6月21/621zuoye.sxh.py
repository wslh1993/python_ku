s=input('输入一个三位数：')
a=len(s)
print(a)
if a==3:
    d=float(s[0])**len(s)+float(s[1])**len(s)+float(s[2])**len(s)
    if float (s)==d:
        print('是水仙花数')
    else:
        print('不是水仙花数')
else:
    print('不是3位数')
'''
遇到问题：
1. s[0] s[1] s[2]为字符串，未改格式前报错，于是改为int(s[0])形式。
2. len(s)输出直接为整形。
3. 用水仙花数153测试，输出d等于153,
但条件s==d一直不成立，经过分析s为chr型。
开头改为s=int(input())后s[0]报错(int不存在len、s[])，s=input()下加int(s)仍不起作用。
最后，将判断语句 s==d改为int(s)==d,再测试，成功。
'''
