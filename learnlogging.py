# coding:utf-8
import sys
import time
import urllib
import urllib2

'''
异常习题：
一
编写with操作类Fileinfo()，定义__enter__和__exit__方法。完成功能：
1.1
在__enter__方法里打开Fileinfo(filename)，并且返回filename对应的内容。如果文件不存在等情况，需要捕获异常。
1.2
在__enter__方法里记录文件打开的当前日期和文件名。并且把记录的信息保持为log.txt。内容格式："2014-4-5 xxx.txt"
'''


class Fileinfo:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            afile = open(self.filename)
        except:
            print "it's error"
            return sys.exc_info()
        else:
            with open(time.strftime("%Y-%m-%d", time.localtime()) + ' ' + self.filename, "w") as bfile:
                for line in afile:
                    bfile.write(line)
            afile.close()
            print "it's else"

    def __exit__(self, type, value, traceback):
        print "miao"


fileclass = Fileinfo("os.txt")
with fileclass as cc:
    pass

'''
二：用异常方法，处理下面需求：
info = ['http://xxx.com', 'http:///xxx.com', 'http://xxxx.cm'....]
任意多的网址
2.1 定义一个方法get_page(listindex)
listindex为下标的索引，类型为整数。 函数调用：任意输入一个整数，返回列表下标对应URL的内容，用try except 分别捕获列表下标越界和url
404
not found
的情况。
2.2 用logging模块把404的url，记录到当前目录下的urlog.txt。urlog.txt的格式为：2013 - 04 - 05
15:50:03, 625
ERROR
http: // wwwx.com
404
not foud、
'''

import logging

def get_page(listindex):
    info = ['http://www.qq.com', 'http://www.baidu.com', 'http://eaveraatgfvxrt.com']
    try:
        aurl = info[listindex]
    except IndexError:
        print "there aren't enough url in the list"
    else:
        try:
            urllib2.urlopen(aurl)
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
            logging.error("error message")
        else:
            return "a"

alog = logging.getLogger()
hdlr = logging.FileHandler("urlog.txt")
logformatter = logging.Formatter("%(asctime)s\n%(levelname)s\n%(message)s")
hdlr.setFormatter(logformatter)
alog.addFilter(hdlr)
alog.setLevel(logging.NOTSET)

get_page(4)

get_page(2)
'''
三：定义一个方法get_urlcontent(url)。返回url对应内容。
要求：
1 自己定义一个异常类，捕获URL格式不正确的情况，并且用logging模块记录错误信息。
2 用内置的异常对象捕获url
404
not found的情况。并且print
'url is not found'
'''

