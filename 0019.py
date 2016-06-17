#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-17 16:18:27
from lxml import etree
import xlrd, os

def load_excel(file_name, sheet_name):
    excel = xlrd.open_workbook(file_name)
    info = excel.sheet_by_name(sheet_name)
    data = []
    for row in range(info.nrows):
        data.append(info.row_values(row))
    return data

def create_xml(file_name, root_ele, sub_ele, cmt, info):
    root = etree.Element(root_ele)
    sub = etree.SubElement(root, sub_ele)
    sub.append(etree.Comment(cmt))
    sub.text = str(info)
    xml = etree.ElementTree(root)
    xml.write(file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')

if __name__ == '__main__':
    file_name = 'numbers.xls'
    sheet_name = 'numbers'
    comment = '数字信息'

    data_info = load_excel(file_name, sheet_name)
    create_xml(os.path.splitext(file_name)[0] + '.xml', 'root', sheet_name, comment, data_info)
