#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-15 17:10:12
import re
import xlwt

if __name__ == '__main__':
    datapat = re.compile(r'\s*"(\d+)"\s*:\s*\["([A-Za-z\u4e00-\u9fa5]+)",(\d+),(\d+),(\d+)\]')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('student', cell_overwrite_ok=True)

    with open('student.txt', encoding='utf-8') as f:
        row = col = 0
        for line in f:
            for items in datapat.findall(line):
                col = 0
                for item in items:
                    ws.write(row, col, item)
                    col += 1
                row += 1

    wb.save('student.xls')
