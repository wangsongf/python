#!/usr/bin/python
#Filename:spider.py
 
import sys
import urllib2
import re
import HTMLParser

class myparser(HTMLParser.HTMLParser):
 def __init__(self):
     HTMLParser.HTMLParser.__init__(self)
 def handle_starttag(self,tag,attrs):
     if (tag == 'a')|(tag == 'img'):#查询标签是否为网址链接或多媒体链接
         for name,value in attrs:
             if (name == 'href')|(name == 'src'):#查询该上面两个标签的属性
                 val = re.search('http://',value)#匹配链接是否为可用链接（有的时候会有空链接的）
                 if val != None:
                      print value     
                       
if sys.argv[1] == '-u':
	content = (urllib2.urlopen(sys.argv[2])).read()#打开网址并读取内容
	con = myparser()
	con.feed(content)#把content的内容，传给myparser分析
else:
	print 'Usage:%s -u url'%sys.argv[0] 
print """                                                                                                                     
-------------------------------------------------------------------------------------------                                                                                                                    
|        **        **        **   ******************   *****************              |
|         **      ****      **    **                   **               *             |
|          **    **  **    **     ****************     *****************              |
|           **  **    **  **      **                   **               *             |
|            ****      ****       **                   **               *             |
|             **        **        ******************   *****************              |
|                                                                                     |
|    *****     **********   **********  ***********    *************  ************    |
|  ********   **        **      **      **        **   **             **         **   |
|   **    **  **        **      **      **         **  **             **         **   |
|    **       **        **      **      **          ** **             **         **   |
|     ***     ***********       **      **          ** *************  ************    |
|       **    **                **      **          ** **             ** **           |
| **     **   **                **      **         **  **             **    **        |
|  ********   **                **      **        **   **             **      **      |
|   ******    **            **********  ***********    *************  **        **    |
|                                                                                     |
|              author:scr@t                              version: 1.0                 |
|                                                                                     |
-------------------------------------------------------------------------------------------
"""   