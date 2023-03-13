import requests
from lxml import etree
import csv

url = 'https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
}

response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
response = response.text
tree = etree.HTML(response)
tr_list = tree.xpath('/html/body/div[5]/div[2]/div/table/tbody/tr')

data_all = []
for i in tr_list:
    data_l = []
    idx = 0
    for j in i.xpath('./td'):
        idx += 1
        if idx >= 7:
            break
        if j.xpath('./text()').__len__() != 0:
            data_l.append(str(j.xpath('./text()')[0]))
    data_all.append(data_l)

data_all = data_all[9:]
print(data_all)
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['包含序号', '债券代码', '债券名称', '计息方式', '债券面额', '年利率'])

    for row in data_all:
        writer.writerow(row)


