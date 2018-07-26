#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:02:35 2018

@author: 3gosc_ai
"""
import socket,json
from threading import Thread
user_list=''
user_name=''
def send(conn):
    global user_name
    while True:
        stat=input('1登录 2退出 3发消息:\n')
        if stat=='1':
            user_name=input('输入姓名:\n').strip()
            data={'stat':'login','from':user_name}
        elif stat=='2':
            if user_name:
                data={'stat':'out','from':user_name}
        else:
            if not user_name:
                continue
            name=input('输入姓名:\n')
            msg=input('输入要发送的消息:\n')
            data={'to':name.strip(),'from':user_name,'msg':msg,'stat':'msg'}
        data=json.dumps(data).encode('utf8')
        conn.send(data)
        if stat==2:
                return 2
def recv1(conn):
    while True:
        data=conn.recv(1024)
        data=json.loads(data.decode('utf8'))
        print(data)
        if data['stat']=='error':
            print('Your sendto %s  msg %s is ERROR')
        elif data['stat']=='out':
            conn.close()
            print('EIXT success')
            return
        elif data['stat']=='login':
            print(data['users'])
        elif data['stat']=='msg':
            print('你收到  %s 的是  %s'%(data['from'],data['msg']))

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',8989))
    t1=Thread(target=send,args=(s,))
    t2=Thread(target=recv1,args=(s,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
        
        
        
        
        
        
        
        
        
        
        
        
