import json
import urllib
from urllib import request, parse

baseurl = 'https://fanyi.baidu.com/sug'

# 用来存放模拟form的数据一定是字典格式
data = {
    # girl是翻译输入的英文内容，应该由用户输入，此处使用硬编码
    "kw": 'girl'
}

# 需要使用parse对data进行编码
data = parse.urlencode(data).encode(encoding='UTF8')

# 我们需要构造一个请求头，请求头部应该至少包含传入的数据长度
# request要求传入的请求是字典格式
headers = {
    # 因为使用post，至少应该包含content-length字段
    'Content-Length':len(data)
}

# 构造一个Request的实例
req = request.Request(url=baseurl, data=data, headers=headers)

# 因为已经构造一个Request的请求实例，对所有的请求信息都可以封装在Request实例中
rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode()
print(json_data)

# 把json字符串转换成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], "---------", item['v'])