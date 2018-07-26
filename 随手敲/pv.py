#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:44:13 2018

@author: 3gosc_ai
"""
class Pv(list):
    def __init__(self,*args):
        self.__value=[]
        for x in args:
            if not isinstance(x,int) and not isinstance(x,float):
                print(' shu ru de value ERROR')
                break
            else:
                self.__value.append(x)
    def __add__(self,other):
        if not isinstance(other,Pv):
            print('ERROR')
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
    def __len__(self):
        return len(self.__value)
    def __str__(self):
        return str(self.__value)
    def __repr__(self):
        return self.__str__()
        
class matrix(object):
    def __init__(self,*args):
        self.__value=[]
        for x in args:
            if not isinstance(x,Pv) :
                x=Pv(*x)
                self.__value.append(x)
            else:
                self.__value.append(x)
    def __add__(self,other):
        if not isinstance(other,matrix):
            print('ERROR')
            return False
        self.__value,other._matrix__value=self.__same(other)
        MC=[]
        for x,y in zip(self.__value,other._matrix__value):
            mc=[]
            for i,j in zip(x._Pv__value,y._Pv__value):
                mc.append(i+j)
            MC.append(mc)
        return matrix(*MC)
    def __len__(self):
        return len(self.__value)
    # jiang liang ge juzhen  yuansu jinxin duiqi
    def __same(self,other):
        M1,M2=self.__value,other._matrix__value
        clom_s=0
        rows_s=0
        if len(M1[0])>len(M2[0]):clom_s=len(M1[0])
        else:clom_s=len(M2[0])
        if len(M1)>len(M2):rows_s=len(M1)
        else:rows_s=len(M2)
        if clom_s>len(M2[0]):
            seq=[int(x) for x in (clom_s-len(M2[0]))*'0']
            for i in range(len(M2)):
                M2[i]._Pv__value.extend(seq)
        else:
            seq=[int(x) for x in (clom_s-len(M1[0]))*'0']
            for i in range(len(M1)):
                M1[i]._Pv__value.extend(seq)
        if rows_s>len(M2):
            for i in range(rows_s-len(M2)):
                M2.append(Pv(*[int(x) for x in '0'*clom_s]))
        else:
            for i in range(rows_s-len(M1)):
                M1.append(Pv(*[int(x) for x in '0'*clom_s]))
        return M1,M2
    def __str__(self):
        value='['
        for x in self.__value:
            value+=str(x)+'\n'
        return value[:-1]+']'
    def __repr__(self):
        return self.__str__()
    
if __name__=="__main__":
    a=[[1,1,1,1],[1,1,1,1]]
    b=[[2,2],[2,2],[2,2]]
    a=matrix(*a)
    b=matrix(*b)
    print(a+b)
    
    
    
    
    
    
    
