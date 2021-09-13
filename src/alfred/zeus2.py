#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: ziling
# date: 2018-04-26

from __future__ import print_function
import StringIO
import base64
import gzip
import os
import re
import traceback
import urllib
import urllib2
import zlib

query = "{query}"

common_headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}


def send_http_request(request_url, request_params, request_headers, request_method):
    if request_method.upper() == "GET":
        if not request_params:
            request = urllib2.Request(request_url, headers=request_headers)
        else:
            url = request_url if request_url.endswith("?") else request_url + "?"
            request = urllib2.Request(url + urllib.urlencode(request_params), headers=request_headers)
        return urllib2.urlopen(request)
    elif request_method.upper() == "POST":
        request = urllib2.Request(request_url, data=urllib.urlencode(request_params), headers=request_headers)
        return urllib2.urlopen(request)
    else:
        print("urllib2不支持的方法[%s]" % request_method)
        return


def decode_response_content(response):
    encoding = response.info().get('Content-Encoding')
    if encoding and encoding.lower() == "gzip":
        compressedstream = StringIO.StringIO(response.read())
        gziper = gzip.GzipFile(fileobj=compressedstream)
        content = gziper.read()
    elif encoding and encoding.lower() == "deflate":
        content = StringIO.StringIO(zlib.decompress(response.read()))
    else:
        content = response.read()
    return content


def get_cookies_from_accounts(username, password):
    # GET请求http://accounts.meili-inc.com/enter获取JSESSIONID
    request_url = "http://accounts.meili-inc.com/enter"
    additional_headers = {
        "Host": "accounts.meili-inc.com",
    }
    request_headers = dict(common_headers, **additional_headers)
    response = send_http_request(request_url, None, request_headers, "GET")
    set_cookie = response.headers.getheaders("Set-Cookie")
    jsessionid = ''
    for tmp in set_cookie:
        if tmp.find("JSESSIONID=") != -1:
            jsessionid = tmp.split('JSESSIONID=')[1].split(';')[0]
    if not jsessionid:
        print("获取JSESSIONID失败！")
        return

    # POST请求http://accounts.meili-inc.com/verify4Web获取mtgk和tls
    request_url = "http://accounts.meili-inc.com/verify4Web"
    request_params = {
        "redirect": "",
        "userName": username,
        "password": password,
        "checkCode": "",
    }
    additional_headers = {
        "Host": "accounts.meili-inc.com",
        "Referer": "http://accounts.meili-inc.com/enter",
        "content-type": "application/x-www-form-urlencoded",
        "x-requested-with": "XMLHttpRequest",
        "origin": "http://accounts.meili-inc.com",
        "Cookie": "JSESSIONID=" + jsessionid,
    }
    request_headers = dict(common_headers, **additional_headers)
    response = send_http_request(request_url, request_params, request_headers, "POST")
    pattern = '"code":"(.*?)".*?"msg":"(.*?)"'
    results = re.findall(pattern, response.read(), flags=re.DOTALL)
    if results and results[0][0] != "200":
        print(results[0][1])
        return
    set_cookie = response.headers.getheaders("Set-Cookie")
    mtgk = ''
    tls = ''
    for tmp in set_cookie:
        if tmp.find("MTGK=") != -1:
            mtgk = tmp.split('MTGK=')[1].split(';')[0]
        if tmp.find("tls=") != -1:
            tls = tmp.split('tls=')[1].split(';')[0]
    if not mtgk or not tls:
        print("获取MTGK或tls失败！")
        return
    return {"jsessionid": jsessionid, "mtgk": mtgk, "tls": tls}


def get_http_result(username, password, param):
    cookie_dict = get_cookies_from_accounts(username, password)
    if not cookie_dict:
        return
    request_url = "http://zeus_new.meili-inc.com/user/search"
    request_params = {
        "domain": "mogujie",
        "third": "",
        "query": param,
        "search": "",
    }
    additional_headers = {
        "Cookie": "JSESSIONID=%s; MTGK=%s; tls=%s" % (
            cookie_dict.get("jsessionid"), cookie_dict.get("mtgk"), cookie_dict.get("tls")),
    }
    request_headers = dict(common_headers, **additional_headers)
    response = send_http_request(request_url, request_params, request_headers, "POST")
    content = decode_response_content(response)
    pattern = ".*?".join(['<span class="pull-right">(.*?)<'] * 9)
    results = re.findall(pattern, content, flags=re.DOTALL)
    if not results or len(results) != 1:
        if os.popen("ping -c 1 www.mogujie.com|grep 10.13", "r").read():
            print("查询失败，当前在线下环境，\n请确认入参或环境是否正确！")
        elif os.popen("ping -c 1 www.mogujie.com|grep 211.159.246.164", "r").read():
            print("查询失败，当前在预发环境，\n请确认入参或环境是否正确！")
        else:
            print("查询失败，当前在线上环境，\n请确认入参或环境是否正确！")
    else:
        user_id = results[0][0].strip()
        user_name = results[0][1].strip()
        if query.isdigit():
            print(user_name, end='')
        else:
            print(user_id, end='')


if __name__ == '__main__':
    try:
        # 用户名密码有两种配置方式：
        #   1、直接配置下面的两个变量；
        #   2、在文件（~/.auth）中配置，第一行用户名，第二行密码，都需要base64加密
        # 两种配置方式选择其一即可；如果同时配置，文件配置会覆盖本脚本中的直接配置。
        username = ""
        password = ""
        auth_file = os.environ['HOME'] + os.sep + ".auth"
        if os.path.exists(auth_file):
            lines = open(auth_file).readlines()
            if len(lines) < 2:
                print("认证配置有误，请检查。")
            username = base64.b64decode(lines[0].strip())
            password = base64.b64decode(lines[1].strip())
        if not username and not password:
            print("用户名或密码未设置。")
        else:
            get_http_result(username, password, query)
    except Exception, e:
        print("发生未知异常：", traceback.format_exc())