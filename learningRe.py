# coding:utf-8
import re
# 1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'
a = re.search(r'"(\S+)"', info)
print a.groups()
# 用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"

# 2 字符串："one1two2three3four4" 用正则处理，输出 "1234"
info2 = "one1two2three3four4"
print re.split("[a-z]+",info2)
# 3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。
texta = "JGood is a handsome boy, he is, clever, and so on..."
b = re.findall(r'(\w*oo\w*)',texta)
print b


######################################
# 要求完成下面2个小功能：
# 1.1 关闭[img]标签
# 1.2 将url()中的["]转为[']
def change(m):
    return m.group() + "</img>"
info3 = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img ' 'src="http://www.baidu.com">ininnnin<img src="http://www.dd.com"> '
patten = re.compile(r'<img \S*?">')
info3 = patten.sub(change,info3)
print info3  #耗时两小时，菜的不行
def change2(m):
    return m.group().replace("\"","'")
print re.search(r'url\(\S*\)', info3).group()
info3 = re.sub(r'url\(\S*\)', change2, info3)
print info3   #更改之后需要赋值

