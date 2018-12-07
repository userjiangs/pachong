from urllib import request, error

# if __name__ == "__main__":
#     url = "httpqqq://wwww.baidu.com"
#     url = "http://www.sipo.gov.cn/www"
#     try:
#         req = request.Request(url)
#         rsp = request.urlopen(req)
#         html = rsp.read().decode()
#         print(html)
#
#     except error.HTTPError as e:
#         print('HTTPError: {0}'.format(e.reason))
#         print('HTTPError: {0}'.format(e))
#
#     except error.URLError as e:
#         print('URLError: {0}'.format(e.reason))
#         print('URLError: {0}'.format(e))
#
#     except Exception as e:
#         print(e)



# 代理服务器
# if __name__ == "__main__":
#     url = "http://www.baidu.com"
#     # 设置代理地址
#     proxy = {'http': '120.194.18.90:81'}
#     # 创建ProxyHandler
#     proxy_handler = request.ProxyHandler(proxy)
#     # 创建Opener
#     opener = request.build_opener(proxy_handler)
#     # 安装Opener
#     request.install_opener(opener)
#
#     # 现在访问就是代理地址访问
#     try:
#         rsp = request.urlopen(url)
#         html = rsp.read().decode()
#         print(html)
#     except error.HTTPError as e:
#         print(e)
#     except error.URLError as e:
#         print(e)
#     except Exception as e:
#         print(e)

#
# # 自动登陆cookie
# from urllib import request, parse
# from http import cookiejar
#
# # 创建cookieJar实例
# cookie = cookiejar.CookieJar()
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
#
#
# def getHomePage():
#     url = "http://www.renren.com/965187997/profile"
#     # 如果已经执行了login函数，则opener已经自动包含相应的cookie值
#     rsp = opener.open(url)
#
#     html = rsp.read().decode()
#     with open("rsp.html","w",encoding='utf-8') as f:
#         f.write(html)
#
#
# if __name__ == "__main__":
#     login()
#     getHomePage()


