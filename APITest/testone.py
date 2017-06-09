#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 8:53
import requests
import unittest
import time
from jiaoben import jball
class testclassone(unittest.TestCase):
    def setUp(self):
        print(111)
        pass
    def test_1(self):
        jball()
        pass
    def tearDown(self):
        print(333)
        pass


if __name__ == '__main__':
    unittest.main()