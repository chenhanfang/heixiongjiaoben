#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 14:09

# 接口信息
API_ALL = {
            '登录接口': {
                            'number': '1',
                            'url': 'http://www.baidu.com',
                            'leixing': 'post',
                            'head': {
                                        'aa': 'bb',
                                        'cc': 'dd',
                                        },
                            'canshu': {
                                        'username': 'Wbfxs001',
                                        'password': '111111Qq',
                                        'grant_type': 'password',
                                    },
                            'qiwang': {
                                        'code': 200,
                                        'name': 'Wbfxs001',
                                        },
                        },

            '退出接口': {
                            'number': '1',
                            'url': 'http://www.baidu.com',
                            'leixing': 'get',
                            'canshu': {
                                        'username': 'Wbfxs001',
                                        'password': '111111Qq',
                                        'grant_type': 'password',
                                      }
            }
}