#!/usr/bin/env Python 

import os, sys, time

 

while True:

time.sleep(4)

try:
#apache 替换
ret = os.popen('ps -C nginx -o pid,cmd').readlines()

if len(ret) < 2:

print "apache 进程异常退出， 4 秒后重新启动"

time.sleep(3)

os.system("service nginx restart")

except:

print "Error", sys.exc_info()[1]