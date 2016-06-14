#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-13 23:44:17
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser
from math import log
import urllib.request
import os

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tag_stack.append(tag)

    def handle_endtag(self, tag, tag_flag = True):
        while tag_flag == True:
            if tag == tag_stack[-1]:
                tag_stack.pop()
                tag_flag = False
            else:
                tag_stack.pop()

    def handle_startendtag(self, tag, attrs):
        if tag == 'img':
            attrs = dict(attrs)
            if attrs['class'] == 'BDE_Image':
                img_srcs.append(attrs['src'])

def get_img(url):
    try:
        response=urllib.request.urlopen(url)
    except HTTPError as e:
        print('Error code:',e.code)
    except URLError as e:
        print('Reason',e.reason)
    else:
        pass

    data = response.read()

    parser = MyHTMLParser()
    parser.feed(data.decode('utf-8'))
    parser.close()

    return img_srcs

def get_path(*directorys, root = os.curdir):
    root += os.sep + os.sep.join(directorys)
    return root

def seq(max_length):
    for i in range(max_length): 
        yield str(i).zfill(int(log(max_length, 10) + 1))

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    tag_stack = []
    img_srcs = []

    imgs = get_img(url)
    dir_path = get_path('baidu','杉本有美')
    i = seq(len(imgs))

    for src in imgs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        src = src.split('?')[0]
        new_name = 'yzhs' + next(i) + '.' + os.path.splitext(src)[1]
        img_path = dir_path + os.sep + new_name

        try:
            conn=urllib.request.urlopen(src)
        except HTTPError as e:
            print('Error code:',e.code)
        except URLError as e:
            print('Reason',e.reason)

        with open(img_path, 'wb') as f:
            f.write(conn.read())
