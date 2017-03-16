# coding:utf-8
import urllib2, re

remod = re.compile(ur'<div class="info "><a href="/video/(?P<av>.+?)/" target="_blank"><div class="title">(?P<title>.+?)</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>(?P<click>.+?)</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>(?P<review>.+?)</span><a href="//space.bilibili.com/\d*" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>(?P<upname>.+?)</span></a></div><div class="pts" title="[\u4e00-\u9fa5]+"><div>(?P<grade>.+?)</div>[\u4e00-\u9fa5]+</div></div>')

bilibiliranking = urllib2.urlopen(r"http://www.bilibili.com/ranking").read()
print bilibiliranking
resultiter = remod.finditer(bilibiliranking)

rankinglist = []
for m in resultiter:
    rankinglist.append(m.groupdict())

print rankinglist
'''
<div class="info "><a href="/video/av9135074/" target="_blank"><div class="title">【贝尔】荒野求生系列（720P超清）（国语版全网最齐）更新至57集</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>27.0万</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>1.0万</span><a href="//space.bilibili.com/43837937" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>A6驾照</span></a></div><div class="pts" title="综合评分"><div>1179503</div>综合评分</div></div>
<div class="info "><a href="/video/av9147506/" target="_blank"><div class="title">爱情公寓op动漫版</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>18.8万</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>841</span><a href="//space.bilibili.com/1939319" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>科学超电磁炮F</span></a></div><div class="pts" title="综合评分"><div>416569</div>综合评分</div></div>
<div class="info "><a href="/video/(?P<av>.+?)/" target="_blank"><div class="title">(?P<title>.+?)</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>(?P<click>.+?)</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>(?P<review>.+?)</span><a href="//space.bilibili.com/\d*" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>(?P<upname>.+?)</span></a></div><div class="pts" title="综合评分"><div>(?P<grade>.+?)</div>综合评分</div></div>

'''