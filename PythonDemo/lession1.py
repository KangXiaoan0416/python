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
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
file = urllib.request.urlopen(url)
data = file.read()
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
# 代理服务器的设置

def use_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
    return data


proxy_addr = "113.56.91.72:80"
data = use_proxy(proxy_addr, "http://www.baidu.com")
print(len(data))







































