import urllib.request
import urllib.parse
# file = urllib.request.urlopen("http://www.baidu.com")
# data = file.read()
# dataLine = file.readline()
# print(dataLine)
# print(data)

# 写文件
filepath = "/home/xiaoan/myweb/part1/"
# fhandle = open(filepath + "1.html", "wb")
# fhandle.write(data)
# fhandle.close()

# 直接爬取一个网页并保存
# urlretrieve 方法会造成本地缓存　用urllib.request.urlcleanup()清除缓存
# filename = urllib.request.urlretrieve("http://www.baidu.com", filename=filepath+"2.html")

# file.info 返回于当前环境有关的信息
# info=file.info()
# print(info)

# 获取状态码
# code=file.getcode()
# print(code)

# 获取当前爬取的url地址
# file.getUrl()


# url处理
# url编码
# path = "http://www.sina.com.cn"
# epath = urllib.request.quote(path);
# print(epath)

# url解码
# p_path = urllib.request.unquote(epath)
# print(p_path)


# ***浏览器模拟 header
# １．build_opener() 修改报头
# url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
# file = urllib.request.urlopen(url)
# data = file.read()
# print(data)
# 模拟火狐浏览器
# headers = ("User-Agent", "")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# file = opener.open(url)
# data = file.read()
# print(data)

# 2.add_header()添加报头
# 创建一个request对象
# req = urllib.request.Request(url)
# 添加报头
# req.add_header('User-Agent', '')
# data = urllib.request.urlopen(req).read()
# print(data)

# 超时设置

# for i in range(1, 100):
#     try:
#         url = "http://yum.iqianyue.com"
#         file = urllib.request.urlopen(url, timeout=1)
#         data = file.read()
#         print(len(data))
#     except Exception as e:
#         print(" 出现异常 --> " + str(e))

# http协议请求实战
# 1.GET请求: 通过url网址传递信息，可以直接在url中写要传递的信息，也可以由表单进行传递．使用表单传递，表单中的信息会自动转为url地址中的数据
# 2.POST请求:　可以向服务器提交数据，是一种比较主流也比较安全的数据传递方式，登录时，经常使用POST请求发数据
# 3.PUT请求:　请求服务器存储一个资源，通常要指定存储的位置
# 4.DELETE请求:　请求服务器删除一个资源
# 5.HEAD请求:　请求获取对应的http报头信息
# 6.OPTIONS请求:　可以获取当前url所支持的请求类型

# get请求示例
# keywd = "韦玮老师"
# key_code = urllib.request.quote(keywd)
# url = "http://www.baidu.com/s?wd=" + key_code
# req = urllib.request.Request(url)
# data = urllib.request.urlopen(req).read()

# fandle = open(filepath+"3.html", "wb")
# fandle.write(data)
# fandle.close()

# POST请求示例

# url = "http://www.iqianyue.com/mypost"
# param = {"name": "kangxiaoan", "pass": "xiaoan0416"}
# postData = urllib.parse.urlencode(param).encode("utf-8")
# req = urllib.request.Request(url, postData)
# req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0")
# file = urllib.request.urlopen(req)
# data = file.read()
# print(file.info())
# fandle = open(filepath + "4.html", "wb")
# fandle.write(data)
# fandle.close()


# -----------------------------代理设置------------------------------------
# 代理服务器的设置 问:此方法是针对http地址代理?

# def use_proxy(proxy_addr, url):
#     import urllib.request
#     proxy = urllib.request.ProxyHandler({'http': proxy_addr})
#     opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
#     return data


proxy_addr = "113.56.91.72:80"
# 问:如何设置境外代理
# jingWai_addr = "127.0.0.1:8118"
# data = use_proxy(proxy_addr, "http://www.baidu.com")
# print(len(data))




# DebugLog实战
# 如何开启DebbugLog
# 1.分别使用
# urllib.request.HTTPHandler() 和
# urllib.request.HTTPSHandler() 讲debuglevel设置为1
# 2.使用urllib.request.build_opener()创建自定义的opener对象,并使用1中设置的值作为参数
# 3.使用urllib.request.install_opener() 创建全局默认的opener对象，这样，在使用urlopen的时候，也会使用我们安装的opener对象
# 4.进行后续操作

# http_hd = urllib.request.HTTPHandler(debuglevel=1)
# https_hd = urllib.request.HTTPSHandler(debuglevel=1)
# opener = urllib.request.build_opener(http_hd, https_hd)
# urllib.request.install_opener(opener)
# url = "http://edu.51cto.com"
# data = urllib.request.urlopen(url)


# ----------------------  异常处理神器  ------------------------------
# UrlError实战
# 问,为什么会有环境信息？ 正常博客不是反爬虫的么，但是下面的这段代码却没有报错
import urllib.error
# try:
#     file = urllib.request.urlopen("http://blog.csdn.net")
    # data = file.read()
    # print(len(data))
    # print(file.info())
# except urllib.error.URLError as e:
#     print(e)
#     # print(e.code) 教程中的e.code属性不存在
    # print(e.filename)
    # print(e.reason)
    # print("异常")
# 产生URlError 异常的原因
# 1.连接不上服务器
# 2.远程Url不存在
# 3.无网络
# 4.触发了HTTPError
# try:
#     file = urllib.request.urlopen("http://blog.csdn.net")
    # data = file.read()
    # print(len(data))
    # print(file.info())
# except urllib.error.HTTPError as e:
#     print(e)

# 状态码含义
# 200 OK 一切正常
# 301 MovedPermanetly 重新定向到临时的Url，永久性
# 302 Found 重新定向到临时的Url,非永久性
# 304 Not Modified 请求的资源未更新
# 400 Bad Request 非法请求
# 401 Unauthorized 请求未经授权
# 403 Forbidden 非法请求
# 404 NOt Found 没有找到页面
# 500 Internal Server Error 服务器内部出现错误
# 501 Not Implemented 服务器不支持实现请求所需要的功能




# 五,正则表达式
# 1.原子 原子是正则表达式中最基本的组成单位,每个正则表达式至少要包含一个原子
# 1)普通字符作为原子 2)非打印字符作为原子-- 用于格式控制的符号 3) 通用字符作为原子 4)原子表
import re
# pattern = "yue"
# string = "http://yum.iqianyue.com"
# result = re.search(pattern, string)
# print(result)

# pattern = "\n"
# string = '''http://yum.iqianyue.com
# http://baidu.com'''
# result = re.search(pattern, string)
# print(result)

# 边界限制元字符 ^和$的应用
# pattern1 = "^abd"
# pattern2 = "^abc"
# pattern3 = "py$"
# pattern4 = "ay$"
# string = "abcdfphp345python_py"
# result1 = re.search(pattern1, string)
# result2 = re.search(pattern2, string)
# result3 = re.search(pattern3, string)
# result4 = re.search(pattern4, string)
# print(result1)
# print(result2)
# print(result3)
# print(result4)

# !!!需要熟悉正则表达式的应用{n,}\{n,m}的含义等
# ()模式单元符, 把几个原子组成一个大原子使用
# >>>敲黑板,重点: 模式修正符
# >>> I:匹配时忽略大小写 M:多行匹配 L:做本地化识别匹配 U:根据Unicode字符及解析字符 S:让.匹配包括换行符,即用了该模式修正后,"."可以匹配任意字符
# pattern1 = "python"
# pattern2 = "python"
# string = "abcdfphp345Python_py"
# result1 = re.search(pattern1, string)
# result2 = re.search(pattern2, string, re.I)
# print(result1)
# print(result2)


# >>>>正则表达式常见函数

# >>re.match() 从源字符的起始位置匹配一个模式
# string = "apythonhellomypythonhispythonourpythonend"
# pattern = ".python."
# result = re.match(pattern, string)
# result2 = re.match(pattern, string)
# result3 = re.search(pattern, string)
# print(result)
# print(result2)
# print(result3)


# >>re.search() ->re.match区别,前者从源字符全文中寻找, 后者从开始位置开始匹配
# >>全局匹配函数 re.compile () 对正则进行预编译, findall() 找出所有的匹配结果
# string = "hellomypythonhispythonyourpythonourpythonend"
# pattern = re.compile(".python.") #预编译
# result = pattern.findall(string) # 找出符合模式的所有结果
# print(result)

# >>re.sub() 替换字符串 re.sub(pattern, rep, string, max)
# result2 = re.sub(pattern, "Python", string, 2)
# print(result2)

# *** 常见实例解析

# ***什么是Cookie
#  HTTP 协议,无状态协议(无法维持会话之间的状态)
#  用Cookie或者Session保存用户登录信息

# 实战 python3: Cookiejar python2:Cookielib
# import http.cookiejar
# url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LawoW"
# postdata = urllib.parse.urlencode({"username":"weisuen","password":"aA123456"}).encode("utf-8")
# req = urllib.request.Request(url, postdata)
# req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
# cjar = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# urllib.request.install_opener(opener)
# data = urllib.request.urlopen(req).read()
# fhandle = open("/home/xiaoan/myweb/part5/1.html", "wb")
# fhandle.write(data)
# fhandle.close()
#
# url2 = "http://bbs.chinaunix.net/"
# req2 = urllib.request.Request(url2, postdata)
# req2.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
# data2 = urllib.request.urlopen(req2).read()
# fhandle = open("/home/xiaoan/myweb/part5/2.html", "wb")
# fhandle.write(data)
# fhandle.close()








