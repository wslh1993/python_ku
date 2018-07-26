class Pv(list):
    def __init__(self,*args):
        self.__value=[]
        for x in args:
            if not isinstance(x,int) and not isinstance(x,float):
                print('error')
                break
            else:
                self.__value.append(x)
    def __add__(self,other):
        if not isinstance(other,Pv):
            print('error')
            return False
        if len(self.__value)>len(other._Pv__value):
            s=len(self.__value)
            other._Pv__value.extend([int(x) for x in '0'*(s-len(other._Pv__value))])
        else:
            s=len(other._Pv__value)
            self.__value.extend([int(x) for x in '0'*(s-len(self.__value))])
        s=[]
        for x,y in zip(self.__value,other._Pv__value):
            s.append(x+y)
        return Pv(*s)
    def __str__(self):
        return str(self.__value)
    def __repr__(self):
        return self.__str__()

a=Pv(1,2,3,4,5,6)
b=Pv(6,5,4,3,2,1)
c=a+b
print(c)

class Pv(list):
    def __init__(self,*args):
        self.__value=[]
        for x in args:
            if not isinstance(x,int) and not isinstance(x,float):
                print('error')
                break
            else:
                self.__value.append(x)
    def __sub__(self,other):
        if not isinstance(other,Pv):
            print('error')
            return False
        if len(self.__value)>len(other._Pv__value):
            s=len(self.__value)
            other._Pv__value.extend([int(x) for x in '0'*(s-len(other._Pv__value))])
        else:
            s=len(other._Pv__value)
            self.__value.extend([int(x) for x in '0'*(s-len(self.__value))])
        s=[]
        for x,y in zip(self.__value,other._Pv__value):
            s.append(x-y)
        return Pv(*s)
    def __str__(self):
        return str(self.__value)
    def __repr__(self):
        return self.__str__()



a=Pv(1,2,3,4,5,6)
b=Pv(6,5,4,3,2,1)
c=a-b
print(c)

