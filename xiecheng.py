# !/usr/bin/env python
# -*- coding=utf-8 -*-

import re
from urllib import request
from bs4 import BeautifulSoup
import os

from pachong import saveFile


class XieChengSpider(object):

    # 初始化爬取的页号、链接以及封装Header

    def __init__(self, pageIndex=1, url="http://you.ctrip.com/asks/dubai1062-k3"):
        self.pageIndex = pageIndex
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
        }

    def fenlei(self,content_list):
        # print(content_list)
        cloth = []
        food = []
        resi = []
        traffic = []
        visa = []
        flight = []
        spot = []
        shopping = []
        weather = []
        cd_card = []
        communication = []
        group = []
        missed = []


        for question in set(content_list):
            print(question)
            for keyword in ['衣服', '穿什么']:
                if keyword in question:
                    cloth.append(question)
                    break
            for keyword in ['美食', '吃什么', '小吃', '好吃的']:
                if keyword in question:
                    food.append(question)
                    break
            for keyword in ['酒店', '宾馆', '住宿', '住哪里', '房间']:
                if keyword in question:
                    resi.append(question)
                    break
            for keyword in ['坐车', '交通', '乘车']:
                if keyword in question:
                    traffic.append(question)
                    break
            for keyword in ['签证', '通行证', '护照', '落地签']:
                if keyword in question:
                    visa.append(question)
                    break
            for keyword in ['飞机', '航班', '航空', '机票', '机场', '转机', '接机', '送机']:
                if keyword in question:
                    flight.append(question)
                    break
            for keyword in ['景点', '美景', '一定要去']:
                if keyword in question:
                    spot.append(question)
                    break
            for keyword in ['购物', '买什么', '纪念品', '免税店', '退税']:
                if keyword in question:
                    shopping.append(question)
                    break
            for keyword in ['天气', '热不热', '气候']:
                if keyword in question:
                    weather.append(question)
                    break
            for keyword in ['信用卡']:
                if keyword in question:
                    cd_card.append(question)
                    break
            for keyword in ['电话卡', '网络', '信号', '上网', 'wifi', 'WIFI']:
                if keyword in question:
                    communication.append(question)
                    break
            for keyword in ['跟团', '参团', '出团', '退团', '随团', '领队']:
                if keyword in question:
                    group.append(question)
                    break

        missed = []
        names = ['吃', '穿', '住', '行', '签证', '航班', '景点', '购物', '天气', '信用卡', '通信', '跟团', '其他']
        types = [food, cloth, resi, traffic, visa, flight, spot, shopping, weather, cd_card, communication, group,
                 missed]
        for question in set(content_list):
            if question not in cloth + food + resi + traffic + visa + flight + spot + shopping + weather + cd_card + communication + group:
                missed.append(question)

        for idx, item in enumerate(types):
            with open('/Users/yinqichang/Project/xieCheng/' + str(names[idx]) + '.txt', 'a+', newline='') as f:
                for row in item:
                    f.write(row)
                    f.write('\n')

    # 请求网页得到BeautifulSoup对象
    def getBeautifulSoup(self, url):
        # 请求网页
        req = request.Request(url, headers=self.header)
        res = request.urlopen(req)
        # 以html.parser格式的解析器解析得到BeautifulSoup对象
        # 还有其他的格式如：html.parser/lxml/lxml-xml/xml/html5lib
        soup = BeautifulSoup(res, 'html.parser')
        return soup

    def saveFile(self, data):
        filename = "/Users/yinqichang/Project/" + "xiecheng.txt"
        if not os.path.exists(filename):
            os.system(r"touch {}".format(filename))  # 调用系统命令行来创建文件
        path = "/Users/yinqichang/Project/" + "xiecheng.txt"
        with open(path, 'a+', encoding='utf-8') as file:
            file.write(data)

    # 读取每个页面上问题
    def getBlogInfo(self, page_index):

        res = []

        # 每页的链接如http://blog.csdn.net/u012050154/article/list/1
        # 所以按pageIndex更新url
        url = self.url+'/p'+str(page_index)+'.html'
        # print(url)
        # 按url解析得到BeautifulSoup对象
        soup = self.getBeautifulSoup(url)
        # 得到目标信息
        for link in soup.find_all('h2'):
            # print(link.get_text())
            if link.get_text() != '旅游攻略导航':
                # print(link.get_text())
                self.saveFile(link.get_text())
                res.append(link.find('span').get_text())
        # print(res)
        return res


    def delete(self):
        f=open("/Users/yinqichang/Project/" + "xiecheng.txt",'a+')
        fnew=open("/Users/yinqichang/Project/" + "xieChenNew.txt",'wb')            #将结果存入新的文本中
        for line in f.readlines():                                  #对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0
            data=line.strip()
            if len(data)!=0:
                fnew.write(data)
                fnew.write('\n')
        f.close()
        fnew.close()

if __name__ == "__main__":
    spider = XieChengSpider()
    pageNum = 50

    for index in range(pageNum):
        print("正在处理第%s页…" % (index + 1))
        blogsInfo = spider.getBlogInfo(index + 1)
        # print(type(blogsInfo))
        spider.fenlei(blogsInfo)

    spider.delete()