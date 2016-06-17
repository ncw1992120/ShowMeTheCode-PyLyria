#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-17 16:09:32
from lxml import etree
import xlrd, codecs, pickle, os

def load_excel(file_name, sheet_name):
    excel = xlrd.open_workbook(file_name)
    student = excel.sheet_by_name(sheet_name)
    data = {}
    for row in range(student.nrows):
        if student.ncols > 2:
            data[student.row_values(row)[0]] = student.row_values(row)[1:]
        else:
            data[student.row_values(row)[0]] = student.row_values(row)[1]
    return data

def create_xml(file_name, root_ele, sub_ele, cmt, info):
    root = etree.Element(root_ele)
    students = etree.SubElement(root, sub_ele)
    students.append(etree.Comment(cmt))
    students.text = str(info)
    student_xml = etree.ElementTree(root)
    student_xml.write(file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')

if __name__ == '__main__':
    file_name = 'city.xls'
    sheet_name = 'city'
    comment = '城市信息'

    student_info = load_excel(file_name, sheet_name)
    create_xml(os.path.splitext(file_name)[0] + '.xml', 'root', sheet_name, comment, student_info)
