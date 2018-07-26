#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:34:09 2018

@author: 3gosc_ai
"""
import os,pickle,json #调用 os ,pickle,json
def login():#登录函数
    if os.path.exists('user.pickle'):#判断有没有user文件
        with open('user.pickle','rb') as f:#读取文件
            users=pickle.load(f)#读取到的用户名密码反序列化放在users
        n=0#定一个放错误次数的变量
        while n<3:#错误大于三次退出循环
            name=input('请输入用户名:')#输入name
            pwd=input('请输入密码:')#输入pws
            if (name,pwd) in users:#如果用户名密码在users里
                print('登陆成功')#登录成功
                return True #返回True
            else:#否则
                n+=1#错误次数+1
        else:
            return False#错误三次跳出 并返回False
    else:#没有文件
        print('无用户,请注册')#输出无用户
        if reg():#先调用reg 注册后
            login()#调用登录
            return True #登陆完 返回 True
        else:#没注册
            return False#返回错误
        
def reg():#注册函数
    try:#排除异常
        users,f=[],False#定义2个存放用户名的变量
        f=open('user.pickle','rb')#把文件存放进变量f
        users_p=pickle.load(f)#把f反序列化存到users_p
        users.extend(users_p)#把users放到users_p
    except:#文件不在
        users=[]#建一个空列表
        if f:
            f.close()#关闭文件
    name=input('请输入要使用的用户名:')#输入用户名存到name
    pwd=input('请输入你的密码:')#输入密码
    with open('user.pickle','wb') as f:#打开文件存在f
        users.append((name,pwd))#把输入的name和pwd 放到users
        pickle.dump(users,f)#把users和f序列化
        print('注册成功')#输出注册成功
    return True#返回True
def search():#查询函数
    if os.path.exists('data.json'):#查看data.json是否存在
        with open('data.json','r') as f:#存在，打开放到f
            data=json.load(f)#反序列化f存在data里
    else:#不存在
        data={}#创建一个空字典
    keyword=input('输入要查找的内容:')#输入要查找的内容放到keyword
    result=data.get(keyword)#在字典data中找到keyword的值放到result
    if result:#如果有值
        return result#返回result的值
    else:#没有值
        print('没找到你要的内容！')#输出没找到你要的内容
        data=input('如果你要录入,请输入“录入”')#把输入的内容放在data
        if data=='录入':#如果data等于录入
            rec()#调用录入函数
        else:#否则
            return False#返回错误
def rec():#录入函数
    if os.path.exists('data.json'):#判断是否存在data.json文件
        with open('data.json','r') as f:#存在读取到f
            data=json.load(f)#反序列化f存入data
    else:#不存在
        data={}#创建一个空字典
    key=input('请输入内容:')#请输入内容存入key
    value=input('请输入内容的翻译:')#请输入内容的翻译存入value
    with open('data.json','w') as f:#打开data.json读取到f
        data[key]=value#把输入的内容和它的翻译 存到字典data中
        json.dump(data,f)#把字典序列化存进data.json
        print('录入成功')#输出录入成功
    return True
def chengxuti():
    if login():
        while True:
            option=input('输入1查询 输入2录入 输入3退出')
            if option=='1':
                data=search()
                if data:print(data)
            elif option=='2':
                rec()
            else:
                exit()
    else:
        exit()

if __name__=='__main__':#主体
    option=input('输入1登录，输入88退出')
    if option=='1':
        chengxuti()
    elif option=='88':
        exit()
    else:
        reg()
        chengxuti()
