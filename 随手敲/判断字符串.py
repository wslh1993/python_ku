s=input()
b=0
if s.isalpha() and s!='':
    for i in s:
        temp=ord(i)
        k.append(temp)
    if max(k)<255:
        print('ying')
    if min(k)>255:
        print('zhong')
    else:
        print('zy')
else:
    print('feifa')
