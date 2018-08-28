# !/usr/bin/env python
# coding=utf-8
import bs4
from bs4 import BeautifulSoup

path='/Users/yinqichang/Downloads/xiecheng.html'
file=open(path,'r',encoding='utf-8')
htmlhandle=file.read()
soup = BeautifulSoup(htmlhandle,'html.parser')
for link in soup.find_all('h2'):
    print(link.get_text())

    