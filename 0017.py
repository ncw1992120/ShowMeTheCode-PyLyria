#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-16 17:58:35
from lxml import etree
import xlrd, codecs, pickle

if __name__ == '__main__':
    excel = xlrd.open_workbook('student.xls')
    student = excel.sheet_by_name('student')
    data = {}
    for row in range(student.nrows):
        data[student.row_values(row)[0]] = student.row_values(row)[1:]
    root = etree.Element('root')
    students = etree.SubElement(root, 'students')
    students.append(etree.Comment("学生信息表\"id\" : [名字, 数学, 语文, 英文]"))
    students.text = str(data)
    student_xml = etree.ElementTree(root)
    student_xml.write('student.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
