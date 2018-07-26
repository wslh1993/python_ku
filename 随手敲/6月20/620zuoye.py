a = input("输入字符串: ")
if a.islower():
    print("a包含的字母全是小写")
elif a.isupper():
    print("a包含的字母全是大写")
elif a.isalpha():
    print("a同时包含且仅包含大小写字母")
elif a.isdigit():
    print("a为纯数字")
elif a.isalnum():
    print("a同时包含大小写字母数字")
else:
    print('a同时包含大小写字母\数字+特殊符号')
'''
判断条件范围小的放前面
范围大的放后面
'''
