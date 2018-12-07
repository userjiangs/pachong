import urllib
from http import cookiejar
from urllib import request, error

# filename = "cookie.txt"
# cookie = cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# rep = request.Request("http://www.baidu.com")
# html = opener.open(rep)
# cookie.save(ignore_discard=True, ignore_expires=True)

# filename = "cookie.txt"
# cookie = cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# rep = request.Request("http://www.baidu.com")
# html = request.urlopen(rep, timeout=2)
# cookie.save(ignore_discard=True, ignore_expires=True)


# cookie = cookiejar.MozillaCookieJar()
# cookie.load("cookie.txt", ignore_expires=True, ignore_discard=True)
# rep = request.Request("http://www.baidu.com")
# opener = request.build_opener(request.HTTPCookieProcessor(cookie))
# html = opener.open(rep)
# print(html.read())

# 代理服务器proxy
