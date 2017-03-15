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
ainfo = [1, 2, 3, 4, 55, 233]
def areturn(x):
    print x
sh = []
for x in ainfo:
    th = threading.Thread(target=areturn, args=[x])
    sh.append(th)
for x in sh:
    x.start()
for x in sh:
    x.join()
print "end2"
'''
习题二：已知列表
urlinfo = ['http://www.sohu.com', 'http://www.163.com', 'http://www.sina.com']
用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。
'''
import urllib
import re
urlinfo = ['http://www.baidu.com', 'http://www.163.com', 'http://www.sina.com']

def openaurl(url):
    a = urllib.urlopen(url)
    webdata = a.read()
    d = re.search(ur"<title>(\S+)</title>", webdata)
    if d == None:
        return None
    print d.groups()[0]   #不知道为何有些网页找不到title


xh = []
for x in xrange(len(urlinfo)):
    th = threading.Thread(target=openaurl,args=[urlinfo[x]])
    xh.append(th)

for x in xh:
    x.start()

for x in xh:
    x.join()

'''
习题三：已知列表
urlinfo = ['http://www.sohu.com', 'http://www.163.com', 'http://www.sina.com']
用多线程的方式分别打开列表里的URL，输出网页的http状态码。
'''
#http状态码： urllib.getcode()
