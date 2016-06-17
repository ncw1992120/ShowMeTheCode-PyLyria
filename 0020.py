#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-17 17:34:51
import os, xlrd

def load_excel(file_name, sheet_name):
    excel = xlrd.open_workbook(file_name)
    info = excel.sheet_by_name(sheet_name)
    data = []
    for row in range(1, info.nrows):
        data.append(info.row_values(row))
    return data

if __name__ == '__main__':
    for path, dirs, files in os.walk(os.curdir):
        if path == os.curdir:
            for file_name in files:
                load_excel(path + os.sep +file_name, file_name)
                
