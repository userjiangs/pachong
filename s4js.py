"""
有道词典查询
"""
import requests

# url = "http://www.baidu.com"
# 两种请求方式
# get 请求

# rsp = requests.get(url)
# print(rsp.text)

# requests请求
# rsp = requests.request("get",url)
# print(rsp.text)


"""
使用参数headers和params
研究返回结果
"""
# 完整访问url是下面的url加上参数构成
url = "http://www.baidu.com/s?"
wd = {
    "wd": '王八蛋'
}
headers = {
    "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36"
}
rsp = requests.get(url, params=wd, headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
# 编码
print(rsp.encoding)
# 请求返回码
print(rsp.status_code)