"""
    目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76

    要求：
        1、请求上述网址的数据
        2、按照要求提取以下字段信息
            title、
            picPath、
            playUrl
        提取下来用 print() 函数打印即可
请在下方编写代码
"""
import requests

# 请求数据
url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
response = requests.get(url=url)
response.encoding = response.apparent_encoding

# 返回是json数据，用.json()转换为json对象
data = response.json()['data']

# 解析数据
for i in range(len(data)):
    print('title:', data[i]['title'], 'picPath:', data[i]['picPath'], 'playUrl:', data[i]['playUrl'])
