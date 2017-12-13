#!/usr/bin/python 
#导入pymysql库
import pymysql

#打开数据库连接
db = pymysql.connect("localhost","root","fnaU2lQw","web" )
 
# 查询前，必须先获取游标 
cur = db.cursor() 
 
# 执行的都是原生SQL语句 
cur.execute("SELECT * FROM learning_logs_topic") 
 
for row in cur.fetchall(): 
    #print(str(row[0])+row[1]+str(row[2])) 
	print(row[0]) 
 
db.close()  