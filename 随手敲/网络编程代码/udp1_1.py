#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:01:01 2018

@author: 3gosc_ai
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',6666))
for x in [b'hello',b'xxxx',b'aaaa']:
    s.sendto(x,('127.0.0.1',8888))
while True:
    print(s.recvfrom(1024))

