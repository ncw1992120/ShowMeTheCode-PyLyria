#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-17 16:18:27
from datetime import datetime
from collections import defaultdict
import os, xlrd, re

def load_excel(file_name, sheet_name):
    excel = xlrd.open_workbook(file_name)
    info = excel.sheet_by_name(sheet_name)
    data = defaultdict(int)
    for row in range(1, info.nrows):
        data[info.row_values(row)[4]] += trans_time(info.row_values(row)[3])
    return data

def trans_time(time_str, pat_str = ''):#输入一个‘x时x分x秒’的字符串，返回一个整数秒数
    time_multi = []
    if '时' in time_str:
        pat_str = r'(\d*)时'
        time_multi.append(3600)
    if '分' in time_str:
        pat_str += r'(\d*)分'
        time_multi.append(60)
    if '秒' in time_str:
        pat_str += r'(\d*)秒'
        time_multi.append(1)

    timepat = re.compile(pat_str)

    time = timepat.match(time_str)

    if time:
        second = 0
        for i in range(len(time_multi)):
            second += time_multi[i] * int(time.group(i + 1))

    return second

if __name__ == '__main__':
    tel_data = {}

    for path, dirs, files in os.walk(os.curdir):
        if path == os.curdir:
            for file_name in files:
                if file_name.endswith('.xls'):
                    tel_data[file_name] = load_excel(path + os.sep +file_name, os.path.splitext(file_name)[0])

    print(tel_data)
