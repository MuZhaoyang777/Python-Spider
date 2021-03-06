"""
爬取《三寸人间》前面十章的小说数据,分别保存在不同的txt文件下

请下下方开始编写代码
"""

import requests
import re


# 请求数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
origin_url = 'https://www.xsbiquge.com'
url = 'https://www.xsbiquge.com/34_34822/'
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding

# 解析数据
data_list = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', response.text, re.S)

for part_url, title in data_list[1:11]:
    # 二次请求数据
    final_url = origin_url + part_url
    res = requests.get(url=final_url, headers=headers)
    res.encoding = res.apparent_encoding
    
    # 二次解析数据
    text = re.findall('<div id="content">(.*?)</div>', res.text, re.S)
    content = text[0].replace('&nbsp;', '').replace('<br />', '\n')
    
    # 保存数据
    with open(title+'.txt', mode='w', encoding='utf-8') as f:
        f.write(content)
    print('下载完成：', title)
