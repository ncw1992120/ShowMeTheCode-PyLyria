#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-13 23:44:17
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser
import urllib.request

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
                img_urls.append(attrs['src'])

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    img_urls = []
    tag_stack = []

    try:
        response=urllib.request.urlopen(url)
    except HTTPError as e:
        print('Error code:',e.code)
    except URLError as e:
        print('Reason',e.reason)

    parser = MyHTMLParser()

    parser.feed(response.read())

    print(img_urls)

    parser.close()
