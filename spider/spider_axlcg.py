# !/usr/bin/env python
# encoding=utf-8

# python爬取 http://www.axlcg.com/ 暖享
import requests
from bs4 import BeautifulSoup
import urllib.request

allurl = []
img = []
count= 0

#伪装成浏览器
def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
    }).content


# 爬取所有图集的url，放到一个list里
def get_all_url():
    firsturl = "http://www.axlcg.com/wmxz/"
    pageindex = 0
    while 1 and pageindex < 20:
        allurldigit = download_page(firsturl)  # 首页面格式化
        allsoup = BeautifulSoup(allurldigit)  # 得到解析后的html
        allpage = allsoup.find('ul', attrs={'class': 'homeboy-ul clearfix line-dot'})
        allpage2 = allpage.find_all('a')
        for allpage2index in allpage2:
            allpage3 = allpage2index['href']
            if allpage3 not in allurl:
                allurl.append(allpage3)
        # 找下一页的url
        next_page1 = allsoup.find('ul', attrs={'class': 'information-page-ul clearfix'})
        next_page2 = next_page1.find_all('li')
        for next_page2_index in next_page2:
            # print(next_page2)
            next_page3 = next_page2_index.find('a')
            # print(next_page3)
            if next_page3.getText() == "下一页" and next_page3.get("href") != None:
                firsturl = next_page3.get("href")
                pageindex = pageindex + 1
                print("总页面" + firsturl)
    print(allurl)
    print(len(allurl))


# 对每一个url进行下载图片
def main():
    get_all_url();
    i = 91
    pagecount = 0;  # 最多八页
    index = 0


    url = download_page(allurl[i])
    soup = BeautifulSoup(url)
    i = i + 1
    while index < 1000 and i < len(allurl):
        # print(allpage)
        # print(soup)
        page0 = soup.find("div", attrs={'class': 'slideBox-detail'})
        # print(page0)
        page = page0.find_all("li")
        # print(page)
        for pageindex in page:
            page2 = pageindex.find("img");
            # print(page2)
            img.append(page2['src'])
        next = soup.find('ul', attrs={'class': 'information-page-ul clearfix'})
        next2 = next.find_all('li')
        for next_url in next2:
            # print(next_url)
            next_page = next_url.find("a")
            if (pagecount < 7 and next_page.getText() == "下一页" and next_page != None and next_page.get("href") != None):
                # print(next_page.get("href"))
                url = next_page.get('href')
                pagecount = pagecount + 1
                url = download_page(url)
                soup = BeautifulSoup(url)
                break;
            elif (pagecount >= 7):
                url = download_page(allurl[i])
                soup = BeautifulSoup(url)
                pagecount = 0
                print(len(img))
                download()
                print("新的页面" + allurl[i])

                i = i + 1
                break
def download():
    #print(len(img))
    global img,count
    print("开始下载图片")
    for m in img:
        urllib.request.urlretrieve(m, "/root/images/" + str(count) + ".jpg")
        count = count+1
        print("正在下载第"+str(count)+"张")
    img = []
    print("下载完毕")

if __name__ == '__main__':
    main()
    download();