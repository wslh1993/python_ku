#coding=utf-8
from threading import current_thread,Thread,local
from time import sleep
# 线程要执行的代码
a=local()
def tingge(name):
    a.name=name
    print(name,current_thread().name)
    sleep(3)

if __name__=='__main__':
    p = Thread(target=tingge,args=('听歌',),name=('线程1'))
    s = Thread(target=tingge,args=('撸代码',),name=('线程2'))
    p.start()
    s.start()
    p.join()
    s.join()
   
