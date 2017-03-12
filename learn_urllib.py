# coding:utf-8
import urllib
google = urllib.urlopen('http://www.baidu.com')
print 'http header:/n', google.info()
print 'http status:', google.getcode()
print 'url:', google.geturl()
for line in google: # 就像在操作本地文件
    print line,
google.close()