#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:05:23 2018

@author: 3gosc_ai
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
while True:
    data,addr=s.recvfrom(1024)
    print(data)
    s.sendto(data,addr)
