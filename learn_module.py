# coding:utf-8
# Editor: bsissb
################################################################
# 习题一：
# 1.1 用time模块获取当前的时间戳.
# 1.2 用datetime获取当前的日期，例如：2013 - 03 - 29
# 1.3 用datetime返回一个月前的日期：比如今天是2013 - 3 - 29 一个月前的话：2013 - 02 - 27
################################################################
import time
import datetime
nowtime = time.time()
datetoday = datetime.date.today()
deltatimea = datetime.timedelta(days = 30)
lastmonthday = datetime.date.today() - deltatimea
print nowtime
print datetoday
print lastmonthday

################################################################
# 习题二:
# 1 用os模块的方法完成ping www.baidu.com操作。
# 2 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，如果有2个
# ".py"的扩展名，则返回一个".py"。
################################################################
import os
os.system("ping www.baidu.com")
def kouzhang(dirpwd):
    os.chdir(dirpwd)
    dirlist = os.listdir(dirpwd)
    return list(set([(adir.split('.'))[-1] for adir in dirlist]))  #到现在了split还用不对

print kouzhang("E:\gemini_images_V7.5.9.0.MAACNDE_20160805.0000.29_6.0_cn")

################################################################
# 习题三：
#
# 定义一个函数xulie(dirname, info)
# 参数：dirname:路径名，info:需要序列化的数据，功能：将info数据序列化存储到dirname路径下随机的文件里。
################################################################
import pickle
def xulie(dirname, info):
    openfile = open(dirname,'w')
    pickle.dump(info,openfile)

