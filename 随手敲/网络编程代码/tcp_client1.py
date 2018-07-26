#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:28:39 2018

@author: 3gosc_ai
"""
import socket #调用服务器
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建一个服务器写IPV4协议 TPC 协议
s.connect(('127.0.0.1',8000))#链接服务器 地址为本地地址 端口为8000
print(s.recv(1024).decode('utf8'))#输出接收到的东西 编码为utf8
while True:#无限循环
    data=input('Please input:')#输入一个东西
    print(data,type(data))#输出输入的东西和它的格式
    s.send(data.encode('utf8'))#以utf8编码格式发送输入的数据
    print(s.recv(1024).decode('utf8'))#输出收到的数据
