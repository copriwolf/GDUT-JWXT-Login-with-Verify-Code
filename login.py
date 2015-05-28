#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
>>>GDUT JWXT Login with Verify Code<<<

Author  = Copriwolf
Version = v1.0
Website = http://or2.in
Created on 2015-5-29.

Just for studying Python.
Read more in README.me

'''

import os
import urllib2
import urllib
import cookielib
import re

Img_URL = 'http://jwgldx.gdut.edu.cn/CheckCode.aspx'
Login_URL = 'http://jwgldx.gdut.edu.cn/Default2.aspx'
username = '3113008066'
password = '**********'


def login():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    # get img
    img_req = urllib2.Request(Img_URL)
    img_response = opener.open(img_req)
    try:
        out = open('code', 'wb')
        # print img_response.read()
        out.write(img_response.read())
        out.flush()
        out.close()
        print 'get code success'
    except IOError:
        print 'file wrong'

    # input code
    img_code = raw_input("please input code: ")
    print 'your code is %s' % img_code

    url = 'http://jwgldx.gdut.edu.cn'
    Request = urllib2.Request(url)
    Responese = urllib2.urlopen(Request)
    PageOutput = Responese.read().decode('gbk')
    Petterm = re.compile('.*?__VIEWSTATE".*?value="(.*?)" />.*?', re.S)
    items = re.findall(Petterm, PageOutput)
    print items[0]

    LoginData = {
        '__VIEWSTATE': items[0],
        'txtUserName': username,
        'TextBox2': password,
        'txtSecretCode': img_code,
        'RadioButtonList1': '%D1%A7%C9%FA',
        'Button1': '',
        'lbLanguage': '',
        'hidPdrs': '',
        'hidsc': ''
    }
    login_header = {
        'Referer': 'http://jwgldx.gdut.edu.cn/default2.aspx',
        'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    }
    login_req = urllib2.Request(
        Login_URL, data=urllib.urlencode(LoginData), headers=login_header)
    login_response = opener.open(login_req)
    print 'login success'
    fout = open("tt.html", "w")
    fout.write(login_response.read())
    fout.close()
if __name__ == '__main__':
    login()
