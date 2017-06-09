#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 14:22
from changliang import ZHCS
from canshuxinxi import API_ALL
from gongju import gj
import requests
# 脚本类，组合工具参数进行请求
gj = gj()
def jball():
    apikeys = API_ALL.keys()
    print(apikeys)
    for key in apikeys:
        apiname = key
        url = API_ALL[key]['url']
        number = API_ALL[key]['number']
        leixin = API_ALL[key]['leixing']
        canshus = gj.listalls(API_ALL[key]['canshu'], ZHCS)
        if leixin == 'post':
            print("======="+" api名称:"+apiname+"=======")
            for cs in canshus:
                mp = requests.post(url=url, data=cs)
                fhcode = str(mp.status_code)
                xysj = str(mp.elapsed.microseconds)
                print("=响应=api编号："+number+"  响应code："+fhcode+"  响应时间:"+xysj)
        if leixin == 'get':
            print("======="+" api名称:"+apiname+"=======")
            for cs in canshus:
                mp = requests.get(url=url, data=cs)
                fhcode = str(mp.status_code)
                xysj = str(mp.elapsed.microseconds)
                print("=响应=api编号："+number+"  响应code："+fhcode+"  响应时间:"+xysj)
jball()