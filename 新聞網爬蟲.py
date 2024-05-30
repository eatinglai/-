# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


new_list = []
url = 'https://money.udn.com/money/index'

## 1.填寫headers
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15'}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
#print(response.text)

## 2.抓取即時區域所有新聞title以及新聞內容連結link，並將每篇新聞的連結link append到new_list內
zone = soup.find_all("li",{"class":"latest story"})
div_tag = soup.find('div', {'id':'tab1'})

soup2 = BeautifulSoup(str(zone), "html.parser")
#a_tags = soup2.find_all("a")['href']
a_tags = soup2.find_all('a')
print(soup2.prettify())

for i in a_tags:
    print('title: {}, link: {}'.format(i.text, 'https://money.udn.com'+i['href']))
    new_list.append('https://money.udn.com'+i['href'])
