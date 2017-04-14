import requests
from bs4 import BeautifulSoup
import re

# 原创申请URL
url = "http://91.t9m.space/forumdisplay.php?fid=19"


# 获取url对应的soup
def getSoup(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    responses = requests.get(url, headers=headers)
    # requests默认编码是ISO-8859-1
    responses.encoding = 'utf-8'
    return BeautifulSoup(responses.text, "html.parser")


#论坛文章黑名单URL
def getNotRequestUrl():
    articleDict = dict()
    articleDict["viewthread.php?tid=143318&extra=page%3D1"] = 1
    articleDict["viewthread.php?tid=132078&extra=page%3D1"] = 2
    articleDict["viewthread.php?tid=136011&extra=page%3D1"] = 3
    articleDict["viewthread.php?tid=125706&extra=page%3D1"] = 4
    return articleDict;

#获取原创申请每一页的文章
def getYuanChuangContent(soup):
    articleDict = getNotRequestUrl();
    contents = soup.body.findAll(
        name='span', attrs={'id': re.compile("thread_*")})
    for items in contents:
        if(items.find(name='a', attrs={'style': ''})):
            for item in items:
                if(not articleDict.get(item.get('href'))):
                    articleDict[item.get('href')] = item.string
                
    return articleDict


# 获取每一个文章中的图片

def getPictureURL(articleUrl):

    articleSoup = getSoup(articleUrl)

    contents = articleSoup.body.findAll(name='img',attrs={'file':re.compile("attachments*")})
    for content in contents:
        file = "http://91.t9m.space/"+content.get('file')





def testMain():
    articleDict = getYuanChuangContent(getSoup(url))

    for key in articleDict:
        
        getPictureURL("http://91.t9m.space/"+key)

testMain()