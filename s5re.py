import urllib
from urllib import parse,request

# 构建代理服务器
import requests

proxies = {
    "http":"address of proxy",
    "https": "address of proxy"
}
rsp = requests.request("get", "http://xxx", proxies = proxies)