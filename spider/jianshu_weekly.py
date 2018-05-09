# -*-coding:utf-8-*-
import csv
import requests
from bs4 import BeautifulSoup

def download_page(url):
    return requests.get(url, headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }).content

base_url = 'http://www.jianshu.com/trending/weekly'

articles = []
data_list = []
for i in range(1, 7):
    url = base_url + '?page={}'.format(i)
    html = download_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    movie_list_soup = soup.find('ul', attrs={'class': 'note-list'})
    for article in movie_list_soup.find_all('li'):
        title = article.find(class_='title').get_text()
        #title = article.find('div', attrs={'class': 'title'}).get_text()
        link = 'http://www.jianshu.com' + article.find(class_='title').get('href')
        author = article.find(class_='nickname').get_text()
        time = article.span['data-shared-at']
        meta = article.find(class_='meta').find_all(['a', 'span'])
        metas = []
        for item in meta:
            metas.append(item.get_text().strip())
        read = metas[0]
        comment = metas[1]
        like = metas[2]
        try:
            money = metas[3]
        except:
            money = '0'
        articles.append([title, author, time, read, comment, like, money, link])

with open('jianshu.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['文章标题', '作者', '时间', '阅读量', '评论', '喜欢', '赞赏数', '文章地址'])
    for row in articles:
        writer.writerow(row)