# coding:utf-8
import urllib
import os
import random
import string
'''
1.定义一个func(url, folder_path)
获取url地址的内容保存到folder_path的文件目录下，并随机生成一个文件名
2.定义一个func(folder_path),合并该目录下的所有文件，生成一个all.txt
3.定义一个func(url),分析该url内容里有多少个链接
4.定义一个func(url),获取？后的参数，并返回成一个dict:
assert('http://url/api?param=2&param2=4') == {'param':'2','param2':'4'}
5.定义一个func(folder).删除该folder下的所有文件
'''
def get_web(url, folder_path):
    assert os.path.isdir(folder_path),"Error, don't find the path"
    try:
        webopen = urllib.urlopen(url)   #检测是否能打开
    except:
        print "Error, can't open url"
    else:
        webget = webopen.read()
        #取小写字母中随机数（4-10）的字母
        filename = ''.join(random.sample(string.lowercase,random.randint(4,11)))
        os.chdir(folder_path)
        aFile = open(filename, 'w')
        aFile.write(webget)
        aFile.close()
        webopen.close()
        return "ok"

print get_web(r'http://cn.bing.com/',r"E:\BaiduYunDownload")
import glob
# def path_all_file(folder_path):
#     assert os.path.isdir(folder_path)
#     with open("all.txt","ab+") as allfile  #需要打开微二进制文件
#     for File in glob.iglob(folder_path+"\*"):
#         openfile = File.open()
#         readFile = openfile.read()
#         allfile.write(readFile)
#         File.close()

# def count_url(url):
#     openpage = urllib.urlopen(url)
#     webget = openpage.read()
#     return len(webget.split("<a href")) - 1
#
# print count_url("https://www.baidu.com/s?wd=aaa&rsv_spt=1&rsv_iqid=0xcf0456bb0001bbde&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E9%259C%259E%25E4%25B9%258B%25E4%25B8%2598&inputT=1629&rsv_t=0c92WD7PSsmvszMeVuTjc0EOJeFvD04%2FrgaTYZlXHvfPGB3fs8Iu2GnlujPAaS48Cmqk&rsv_pq=9548a02e0001a319&rsv_sug3=4&bs=%E9%9C%9E%E4%B9%8B%E4%B8%98")
# #还没学正则不是很懂，根据视频答案无法达到目的

def url_dict(url):
    if not (url.startswith("https") or url.startswith("http")):
        return "传入url格式不对"
    else:
        question_mark = url.find(r"?")
        print question_mark
        needlist = url[question_mark+1:].split("&")
        needdict = dict([tuple(x.split("=")) for x in needlist])
        return needdict


print url_dict(r'http://url/api?param=2&param2=4')

def delete_all(folder):
    assert os.path.isdir(folder),"Error, it's not a folder"
    os.chdir(path)
    pass #用os.dir(path)得到当前路径下的所有文件名的列表