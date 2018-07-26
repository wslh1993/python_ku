def smj(*z):
    if len(z)==3:
            print(z)
            a=z[0]
            b=z[1]
            c=z[2]
            print(a,b,c)
            if a+b>c and a+c>b and c+b>a and abs(a-b)<c and abs(a-c)<b and abs(b-c)<a:
                p=(a+b+c)/2
                print(p)
                s=(p*(p-a)*(p-b)*(p-c))**0.5
                print(s)
            else:
                print('不能构成三角形')
    elif len(z)==2:
        d=z[0]
        e=z[1]
        s=(d*e)/2
        print(s)
    else:
        print('边数不正确')
    return s
