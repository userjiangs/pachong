# from urllib import request, parse
# from http import cookiejar
# # 创建filecookiejar实例
# filename = "cookie.txt"
# cookie = cookiejar.MozillaCookieJar(filename)

# # 生成cookie的管理器
# cookie_handler = request.HTTPCookieProcessor(cookie)
# # 生成http管理器
# http_handler = request.HTTPHandler()
# # 生成https管理器
# https_handler = request.HTTPSHandler()
# # 创建请求管理器
# opener = request.build_opener(http_handler, https_handler, cookie_handler)
# def login():
#     """
#     负责初次登陆，
#     需要用户名密码，
#     :return:
#     """
#     url = "http://www.renren.com/PLogin.do"
#     # 需要从登陆form的两个对应的input中获取name属性
#     data = {
#         'email':"13119144223",
#         'password': '123456'
#     }
#     # 将数据进行编码
#     data = parse.urlencode(data)
#     # 创建一个请求对象
#     req = request.Request(url, data=data.encode())
#     # 使用opener发起请求
#     rsp = opener.open(req)
#     # 保存cookie到文件
#     # ignor_discard表示即使cookie将被丢弃也要保存下去
#
#     cookie.save(ignore_discard=True, ignore_expires=True)
#
#
# if __name__ == "__main__":
#     login()




# 读取cookie

from urllib import request, parse
from http import cookiejar
# 创建filecookiejar实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
cookie.load("cookie.txt", ignore_expires=True, ignore_discard=True)
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def getHomePage():
    url = "http://www.renren.com/965187997/profile"
    # 如果已经执行了login函数，则opener已经自动包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html","w",encoding='utf-8') as f:
        f.write(html)


if __name__ == "__main__":
    getHomePage()