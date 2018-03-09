# -*- coding: utf-8 -*-
import os      
import sys    
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup  
import requests  
import lxml
import uuid
#import pdb


def judge_folder(path):
    if os.path.isdir(path):
        return False
    else:
        os.mkdir(path)
        return True

def save_pic(url,path):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    filename = path +'/'+str(uuid.uuid1())+'.jpg'
    print(filename)
    with open(filename,"wb") as f:
        f.write(response.read())

def get_mei_channel(url):  
    web_data=requests.get(url)  
    web_data.encoding='gb2312'
    soup=BeautifulSoup(web_data.text,'lxml')
    channel=soup.select('body span a')
    return channel

def get_mei_info(url):  
    web_data=requests.get(url)  
    web_data.encoding='gb2312'
    soup=BeautifulSoup(web_data.text,'lxml')
    info=soup.select('body div.pic a')
    return info

def get_mei_pic(url):  
    web_data=requests.get(url)  
    web_data.encoding='gb2312'
    soup=BeautifulSoup(web_data.text,'lxml')
    pic=soup.select('body p img')
    titlelist=soup.select('body div h2 a')
    for list in titlelist:
        path_folder = format(list.get_text())
        path = root_folder + path_folder #path_folder.encode('utf-8')
        print('创建文件夹>>>'+ path_folder +'>>>')#path_folder.encode('utf-8')
        if judge_folder(path):
            print('***开始下载啦！！***')
        else:
            pic =[]
            print('***文件夹已存在，即将开始保存下一个页面***')
    return pic ,path
 

def MeiZiTuSpider(url):
    channel_list = get_mei_channel(url)
    print(channel_list)
    for channel in channel_list:
        channel_url = (channel.get('href'))
        channel_title = (channel.get('title'))
        #pdb.set_trace() # 运行到这里会自动暂停
        print('***开始查找 '+channel_title +' 分类下的妹子图***')#channel_title.encode('utf-8')
        info_list = get_mei_info(channel_url)
        for info in info_list:
            info_url = (info.get('href'))
            pic_list,path = get_mei_pic(info_url)
            for pic in pic_list:
                pic_url = (pic.get('src'))
                save_pic(pic_url,path)


root_folder = 'MEIZITU/'
url='http://www.meizitu.com/'

if __name__ == "__main__":
    if os.path.isdir(root_folder):
        pass
    else:
        os.mkdir(root_folder)
    MeiZiTuSpider(url)
    
    print('****MeiZiTuSpider@Awesome_Tang****')