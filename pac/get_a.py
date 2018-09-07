from urllib import request
from chardet import detect
from bs4 import BeautifulSoup
from lxml import etree
import gzip
#获取网页
req = request.Request('http://xian.esf.fang.com/')
req = request.urlopen(req)
data = req.read()
#解压
try:
    if 'gzip' in req.getheader('Content-Encoding'):
        data = gzip.decompress(data)
except Exception:
    pass
#转码
data = data.decode(detect(data)['encoding'],errors='ignore')
#创建etree对象
sel = etree.HTML(data)
#用Xpath定位所有该位置a标签的title
titles=sel.xpath('//*[@dataflag="bg"]/dd[1]/h4/a/@title')
#循环写入文件
for i in titles:
    with open('titles.txt','a',encoding='utf8') as f:
        f.write(i)
        f.write('\n')
