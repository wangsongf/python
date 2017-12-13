#!/usr/bin/python 
#导入requests库(请求和页面抓取)
import requests
#导入正则库(从页面代码中提取信息)
import re
#导入科学计算库(拼表及各种分析汇总)
import pandas as pd
#导入pymysql库
import pymysql

#设置请求中头文件的信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'https://www.baidu.com/'
}

#抓取并保存页面信息
r=requests.get('http://www.p2peye.com/shuju/ptsj/',headers=headers)
html=r.content
#对抓取的页面进行编码
html=str(html, encoding = "GBK")
#查看抓取的页面源码
html
#使用正则提取title字段信息
title=re.findall(r'"return false".*?title="(.*?)"',html)
print(title)
#使用正则提取total字段信息
total=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="total">(.*?)</td>',html,re.S) ] 
print(total)
#使用正则提取rate字段信息
#rate=re.findall(r'"rate">(.*?)<',html)
rate=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="rate">(.*?)</td>',html,re.S) ] 
print(rate)
#使用正则提取pnum字段信息
#pnum=re.findall(r'"pnum">(.*?)人<',html)
pnum=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="pnum">(.*?)</td>',html,re.S) ] 
print(pnum)
#使用正则提取cycle字段信息
#cycle=re.findall(r'"cycle">(.*?)月<',html)
cycle=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="cycle">(.*?)</td>',html,re.S) ] 
print(cycle)
#使用正则提取plnum字段信息
#p1num=re.findall(r'"p1num">(.*?)人<',html)
p1num=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="p1num">(.*?)</td>',html,re.S) ] 
print(p1num)
#使用正则提取fuload字段信息
#fuload=re.findall(r'"fuload">(.*?)分钟<',html)
fuload=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="fuload">(.*?)</td>',html,re.S) ] 
print(fuload)
#使用正则提取alltotal字段信息
#alltotal=re.findall(r'"alltotal">(.*?)万<',html)
alltotal=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="alltotal">(.*?)</td>',html,re.S) ] 
print(alltotal)
#使用正则提取captial字段信息
#capital=re.findall(r'"capital">(.*?)万<',html)
capital=[ x.replace('\n', '').strip() for x in  re.findall(r'<td class="capital">(.*?)</td>',html,re.S) ] 
print(capital)

#打开数据库连接
db = pymysql.connect("localhost","root","fnaU2lQw","web" )

# 使用 cursor() 方法创建一个游标对象 cursor
cur = db.cursor()

#创建一个表
#sql1 = "CREATE TABLE wdty6( title varchar(255), total varchar(255), rate varchar(255), people_num varchar(255), cycle varchar(255), people_lend_num varchar(255), full_load varchar(255), all_total varchar(255), capital varchar(255)) "
 
# 使用 execute() 方法执行 SQL 语句
#cur.execute(sql1)

#向表中创建新的记录
for i in range(len(title)):
	sql="INSERT INTO `wdty6`(`title`, `total`, `rate`, `people_num`, `cycle`, `people_lend_num`, `full_load`, `all_total`, `capital`)VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s);"
	values=(title[i],total[i],rate[i],pnum[i],cycle[i],p1num[i],fuload[i],alltotal[i],capital[i])
	print(values)
	exit
	cur.execute(sql,values)
	db.commit()


#设置查询语句
sql1="SELECT * FROM wdty6 where cycle>0.6;"
 
# 使用 execute() 方法执行 SQL 查询 
cur.execute(sql1)

#使用fetchall()方法获取所有数据
data = cur.fetchall()


#将获取数据
import pandas as pd
columns=["title", "total", "rate", "people_num", "cycle", "people_lend_num", "full_load", "all_total", "capital"]
df = pd.DataFrame(list(data),columns=columns)

#查看数据表
df.head()

# 关闭数据库连接
db.close()