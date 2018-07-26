#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 13:32:07 2018

@author: 3gosc_ai
"""
import socket,json#调用socket 和 json模块
from threading import Thread#调用线程模块
user_list={}#建一个空用户列表
def recv(conn):#服务器的接收函数
    global user_list#用户列表全局变量
    while True:#无限循环
        data=conn.recv(1024)#接收1k数据放在data
        print(data,addr)#打印data和地址
        data1=json.loads(data.decode('utf8'))#反序列化data放到data1
        if data1['stat']=='msg':#如果data1 stat 的值是msg
            if user_list.get(data1['to']):#如果用户列表可以取到值
                user_list.get(data1['to']).send(data)#发送
            else:#f否则
                data1['stat']=='error'#如果data1 stat 的值是error
                conn.send(json.dumps(data1).encode('utf8'))#把data1序列化发过去
        elif data1['stat']=='login':#如果data1 stat 的值是login
            data={'stat':'login','users':list(user_list.keys())}#
            user_list[data1['from']]=conn
            for x in user_list.values():
                x.send(json.dumps(data).encode('utf8'))
        elif data1['stat']=='out':
            user_list[data1['from']].close()
            del user_list[data1['from']]
            data={'stat':'login','users':user_list.keys()}
            for x in user_list.values():
                x.send(json.dumps(data).encode('utf8'))
                conn.close()
            return False
    
if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',8989))
    s.listen(5)
    while True:
        conn,addr=s.accept()
        t=Thread(target=recv,args=(conn,))
        t.start()
        
