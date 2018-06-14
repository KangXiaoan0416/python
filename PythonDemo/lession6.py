# 手写python爬虫

# ------------------------------
# 京东手机分类页面爬取
import re
import urllib.request
import urllib.error

#
# def craw(url, page):
#     html1 = urllib.request.urlopen(url).read();
#     html1 = str(html1)
#     pat1 = '<div id="plist".+?<div class="page clearfix">'
#     result1 = re.compile(pat1).findall(html1)
#     result1 = result1[0]
#     pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
#     imageList = re.compile(pat2).findall(result1)
#     x = 1
#     for imgUrl in imageList:
#         imageName = "/home/xiaoan/myweb/part6/img1/" + str(page) + str(x) + ".jpg"
#         imageUrl = "http://" + imgUrl;
#         try:
#             urllib.request.urlretrieve(imageUrl, filename=imageName)
#         except urllib.error.URLError as e:
#             if hasattr(e, "code"):
#                 x += 1
#             if hasattr(e, "reason"):
#                 x += 1
#         x += 1
#
#
# for i in range(1, 79):
#     url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
#     craw(url, i)


# ２.链接爬虫实战


# def getLink(url):
#     # 模拟浏览器
#     headrs = ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
#     opener = urllib.request.build_opener()
#     opener.addheaders = [headrs]
#     # 将opener安装为全局
#     urllib.request.install_opener(opener)
#     file = urllib.request.urlopen(url)
#     data = str(file.read())
#     # 根据表达式构建好链接表达式
#     pat = '(https?://[^\s)";]+\.(\w|/)*)'
#     link = re.compile(pat).findall(data)
#
#     # 去除重复元素
#     link = list(set(link))
#     return link
#
#
# # 要爬取的网页链接
# url = 'http://blog.csdn.net/'
# # 获取对应网页中包含的链接地址
# linkList = getLink(url)
# # 通过for循环分别遍历输出获取到的链接地址到屏幕上
# for link in linkList:
#     print(link[0])


# ３.糗事百科爬虫实战


# def getcontent(url, page):
#     # 模拟成浏览器
#     headers = ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
#     opener = urllib.request.build_opener()
#     opener.addheaders = [headers]
#     urllib.request.install_opener(opener)
#
#     data = urllib.request.urlopen(url).read().decode("utf-8")
#     # 构建对应用户提取的正则表达式
#     userpat = '<h2>(.*?)</h2>'
#     # 构建段子内容提取的正则表达式
#     contentpat = '<div class="content.*?span>(.*?)</span>'
#
#     # 寻找出所有的用户
#     userlist = re.compile(userpat, re.S).findall(data)
#
#     # 寻找出所有的内容
#     contentlist = re.compile(contentpat, re.S).findall(data)
#
#     x = 1
#     for content in contentlist:
#         content = content.replace("\n", "")
#
#         name = "content" + str(x)
#
#         # 通过exec() 函数实现用字符串作为变量名并赋值 exec()->执行括号中的语句
#         exec(name+'=content')
#         x+=1
#     y = 1
#     for user in userlist:
#         name = "content" + str(y)
#         print("用户" + str(page) + str(y) + "是:" + user)
#         print("内容是：")
#         exec("print(" + name + ")")
#         print("\n")
#         y+=1
#
#
# for i in range(1, 2):
#     url = "http://www.qiushibaike.com/8hr/page/" + str(i)
#     getcontent(url, i)
#

# 设置模拟浏览器
def addheader():
    # 模拟成浏览器
    headers = ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

# 4.微信爬虫实战




























































