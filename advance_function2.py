# coding:utf-8
import urllib
# 1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
def get_num(num):
    assert isinstance(num, list), "Error, the parameter should be a list"
    for x in num:
        assert isinstance(x, int), "Error, not all are int in list" #数字类型不止有int
    return [x for x in num if x % 2 == 0]

# 2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
def get_page(url):
    openpage = urllib.urlopen(url)
    return openpage.readlines()

print get_page(r"http://www.baidu.com")
#3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
'''#想太多试图考虑列表中有列表的情况并使用迭代，大失败（
def func(*lists):
    maxer = []
    isallint = 1
    for lista in lists:
        if isinstance(lista, list):
            maxer.extend(lista)
            isallint = 0
        elif isinstance(lista, int):
            maxer.append(lista)
    if isallint == 1:
        return max(maxer)
    elif isallint == 0:
        return func(maxer)


print func([3, 5, 3, 5, 7], [2, 4, 5])
'''
def func(*lists):
    listmax = []
    for lista in lists:
        assert isinstance(lista, list), "Error not lists"
        listmax.extend(lista)
    print max(listmax)


print func([3, 5, 3, 5, 7], [2, 4, 5])
'''
传入lista
1.检查Lista中是否有list 是：单独列出 否：拿出到非list中
2.是：再次检查单独列出的list中是否有list
否：比较大小得到max
'''
# 4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
import glob
import os
def get_dir(f):
    dir_list = []
    os.chdir(f) #工作目录到f
    all_dir = glob.iglob(f+r'\*')
    for dirs in all_dir:
        if os.path.isdir(dirs):
            dir_list.append(dirs)
    return dir_list

print get_dir(r"E:")
