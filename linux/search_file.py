#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
def search(folder, filter, allfile):
    folders = os.listdir(folder)
    for name in folders:
        curname = os.path.join(folder, name)
        isfile = os.path.isfile(curname)
        if isfile:
            ext = os.path.splitext(curname)[1]
            count = filter.count(ext)
            if count>0:
                cur = myfile()
                cur.name = curname
                allfile.append(cur)
        else:
            search(curname, filter, allfile)
    return allfile