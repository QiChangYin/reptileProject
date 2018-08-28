#coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
import datetime
import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
#reload(sys)
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
#sys.setdefaultencoding("utf-8")
import json
 # 美团网



def meituan( url):
    # 美团评价采用动态网页，访问对应的接口解析JSON即可
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    # 定义源
    source = u'美团'

    # 访问网页
    req = urllib.request.get(url,headers = headers)

    # 获取内容
    charset = req.encoding
    content = req.text.encode(charset).decode('utf-8')

    # 转化为JSON对象
    json_con = json.loads(content)

    # 获取评论列表
    comment_list = json_con['data']['commentDTOList']
    print(comment_list)

    # 根据url中的poiId判断地点
    if url[58:60] == '16':
        spot = '伊芦山'
    else:
        spot = '大伊山'

    # 获取具体内容
    for comment in comment_list:

        # 地点
#            spot = comment['menu'][:5]
        # 评论时间
        comment_time = datetime.datetime.strptime(comment['commentTime'],'%Y年%m月%d日')
        time = datetime.datetime.strftime(comment_time,"%Y-%m-%d %H:%M")
        # 用户
        userid = comment['userName']
        # 内容
        content = comment['comment']
        # 星级
        star = comment['star']/10
        print(comment_list,star,userid,time)

        if time > self.get_last_time(source,spot):
            self.saveData(source,spot,time,userid,content,star)

if __name__ == "__main__":
    meituan()