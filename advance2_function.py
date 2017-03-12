# coding:utf-8
#习题：
import os
#1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def intmaxmin(*a):
    """ get some int and return its biggest and minimum in tuple"""
    for x in a:
        if not isinstance(x, int):
            return "Error, have error argument"
        else:
            pass
    return (max(a), min(a))

print intmaxmin(3,4,6,2,4,6)
#2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def manlen(*a):
    """ get some string(s) and return longest"""
    lenmax =[]
    for x in a:
        if not isinstance(x, str):
            return "Error, not str in the parameter"
        else:
            lenmax.append(len(x))
    return a[lenmax.index(max(lenmax))]
print manlen("ejorhoa","ejro3io4nf")
#3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
#例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。

def get_doc(module):
    os.popen('python -m %s' %(module))
    print help(module)

#4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
def get_text(f):
    files = open(unicode(f, "utf-8"), "r") #或者改为utf=8
    a = files.read()
    return a

print get_text(r"E:\BaiduYunDownload\老王Python\code\基础数据类型\import_File.txt") #中文路径用u 路径用r确保不会变
#5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
import glob
def get_dir(folder):
    return glob.iglob(unicode(folder,"utf-8"))

print [x for x in get_dir(r"E:\BaiduYunDownload\老王Python\code\*")]