from urllib import request
import urllib


# if __name__ == '__main__':
#     url = 'https://blog.csdn.net/i_peter/article/details/53380334'
#     rsp = urllib.request.urlopen(url)
#
#     html = rsp.read()
#     print(type(html))
#
#     # 如果想把bytes内容转换成字符串，需要解码
#     html = html.decode()
#     print(html)
import chardet

if __name__ == '__main__':
    url = 'https://blog.csdn.net/i_peter/article/details/53380334'
    rsp = urllib.request.urlopen(url)

    html = rsp.read()
    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode(cs.get('encoding', 'utf-8'))
    print(html)