#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'mayi'

import csv

#写：追加
row = ['5', 'hanmeimei', '23', '81']
out = open("test1.csv", "a", newline = "")
csv_writer = csv.writer(out, dialect = "excel")
csv_writer.writerow(row)