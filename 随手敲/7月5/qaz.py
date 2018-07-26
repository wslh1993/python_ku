#coding=utf-8
from multiprocessing import Process
import os
from time import sleep
# 子进程要执行的代码
def tingge(name):
    print('正在听歌，name= %s ,pid=%d' % (name, os.getpid()))
    sleep(7)
    print('听歌结束')
def ludaima(name):
    print('正在撸代码，name= %s ,pid=%d' % (name, os.getpid()))
    sleep(4)
    print('撸完代码')
if __name__=='__main__':
    print('父进程 %d.' % os.getpid())
    p = Process(target=tingge, args=('听歌',))
    s = Process(target=ludaima, args=('撸代码',))
    print('子进程将要执行')
    p.start()
    s.start()
    p.join()
    s.join()
    print('子进程已结束')


