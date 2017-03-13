# coding:utf-8
import threading
import time


def test(p):
    time.sleep(0.001)
    print p


ts = []
for i in xrange(0, 15):
    th = threading.Thread(target=test, args=[i])  # i作为参数引入test
    ts.append(th)
    # 依次生成
for i in ts:
    i.start()
    # 依次启动
for i in ts:
    i.join()
    # 依次join
print "end"
'''
习题一：已知列表
info = [1, 2, 3, 4, 55, 233]

生成6个线程对象, 每次线程输出一个值，最后输出："the end"。
'''
info = [1, 2, 3, 4, 55, 233]


def areturn(x):
    return x


athlist = []
for i in xrange(6):
    th = threading.Thread(target=areturn, args=info)
    athlist.append(th)
for i in athlist:
    i.start()

for i in athlist:
    i.join()

'''
习题二：已知列表
urlinfo = ['http://www.sohu.com', 'http://www.163.com', 'http://www.sina.com']
用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。
'''
urlinfo = ['http://www.sohu.com', 'http://www.163.com', 'http://www.sina.com']

'''
习题三：已知列表
urlinfo = ['http://www.sohu.com', 'http://www.163.com', 'http://www.sina.com']
用多线程的方式分别打开列表里的URL，输出网页的http状态码。
'''
