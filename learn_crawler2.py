# coding:utf-8
from bs4 import BeautifulSoup
import urllib

url = r"http://news.ifeng.com/hotnews/"
a = urllib.urlopen(url).read()
b = a.decode("utf-8").encode("utf-8")
c = BeautifulSoup(b, "lxml")  # 被建议这样搞不是很懂
print c