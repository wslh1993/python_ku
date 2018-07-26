#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:18:28 2018

@author: 3gosc_ai
"""
import socket#调用服务器
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建一个服务器写IPV4协议 TPC 协议
s.bind(('127.0.0.1',8000))#绑定一个器地址为本地地址 端口为8000
s.listen(1)#监听 
while True:
    conn,addr=s.accept()#接受链接及返回
    conn.send(b'Please speak')#给链接上的用户发送文字
    while True:#一直接收
        data=conn.recv(1024).decode('utf8')#接收 用户发送的信息
        print(addr,data)#输出用户发送的信息
        conn.send(('You send is:'+data).encode('utf8'))#给链接的用户发送

    conn.close()#断开连接
