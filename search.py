#author:Scr@t 
#--coding:utf-8--
import sys
import re

f = open(sys.argv[2],'r')  #以只读的方式打开文件
num = 0                                       #初始化计数变量
while True:
	line = f.readline()             #读取一行信息
	string = re.search(sys.argv[1],line)      #比较这一行字符有没有相同的
	num += 1                                  #每读一行，num加1
	if string != None:                        #判断re.search的返回值
		print "%d : %s"%(num,line)
f.close()