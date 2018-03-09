#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
dir = "/mnt/Packages"
class Packages:
    def __init__(self,srcdir,desdir):
        self.sdir=srcdir
        self.ddir=desdir
    def check(self):
        print('program start...')
        for dirpath, dirnames, filenames in os.walk(self.sdir):  #www.111cn.Net  #遍历文件
            for filename in filenames:
                thefile=os.path.join(dirpath,filename)            #文件的绝对地址
                try:
                    if os.path.splitext(thefile)[1]=='.txt':      #筛选.rpm格式的文件
                        #print('Fount rpm package: ' + thefile)
                        #if 'inspuer' in os.popen('rpm -qpi ' + thefile).read().rstrip():
                        print('Found error package: ' + thefile)
                        shutil.copy(thefile, self.ddir)  #将错误文件复制到desdir目录
                        f = open('list.txt', 'a')    #将错误文件列表写入到list.txt
                        f.write(filename + ' ')
                        f.close()
                except IOError:
                    #print(err)
                    sys.exit()
 
if __name__ == '__main__':
    dir=Packages('/root/python/linux','/root/python/linux/newdir')   #源目录为/mnt/cdrom，目标目录为/mnt/erpm
    dir.check()