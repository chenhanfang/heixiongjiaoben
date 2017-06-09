#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 14:11

class gj():

    def listalls(self, csTrue,  csFalse):
        fzgcs = []  # 得到cycanshu的key，将所有非正规参数放在一个list中
        listall = []  # 保存参数dict 为 list
        zhcs = dict(csTrue)
        listall.append(csTrue)
        aaa = list(csFalse.keys())
        for i in aaa:
            bbb = csFalse[i]  # 得到具体参数list
            for k in bbb:
                fzgcs.append(k)  # 便利每一个参数加入fzgcs列表

        zhcskey = list(zhcs.keys())  # 拿到将要进行组合的参数
        for i in zhcskey:
            a = zhcs[i]  # 保留原有的参数值，下面替换完后复原正确参数
            for k in fzgcs:
                zhcs[i] = k
                listall.append(str(zhcs))
            # 循环完后复原正确参数
            zhcs[i] = a
        return listall
