"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为csv格式
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""

import requests
import csv
import re
import json

# 请求数据
url = 'https://temp.163.com/special/00804KVA/cm_yaowen20200213.js?callback=data_callback'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'authority': 'news.163.com',
}
res = requests.get(url=url, headers=headers)
res.encoding = res.apparent_encoding

# 解析数据
data = re.findall('data_callback\((.*?)\)', res.text, re.S)[0]
json_data = json.loads(data)
# print(json_data)


# 保存数据
with open('网易新闻.csv', mode='w', encoding='utf-8', newline='') as f:
    # csv保存数据的写入
    csv_writer = csv.writer(f)
    for li in json_data:
        title = li['title']
        channel_name = li['channelname']
        doc_url = li['docurl']
        img_url = li['imgurl']
        source = li['source']
        tlink = li['tlink']
        csv_writer.writerow([title, channel_name, doc_url, img_url, source, tlink])
