#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 14:09
# 常用参数不传，为空，整形，浮点，字符串，object,过短，超长，sql注入
objects1 = 'xxxx'
objects2 = 'ssss'

ZHCS = {
            '为空': [''],
            '整形': [10, 23, 44, 88, 99],
            '浮点': [1.11, 2.342, -1.03],
            '字符串': ['aaaa', 'bbbb', 'cccc','dddd'],
            'object': [objects1, objects2],
            '过短': ['1', '0'],
            '超长': ['11111111111111111111111111111111111111111111111'],
            'sql注入': [';and 1=1 ;and 1=2', ";and (select count(*) from sysobjects)>0 mssql", ";and 1=(select IS_SRVROLEMEMBER('sysadmin'));--"],
         }