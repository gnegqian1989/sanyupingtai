#!/usr/bin/python
#coding:utf-8

import requests
import json
import unittest
import sys
sys.path.append(r'G:\zi\sanyujieko\san_config')
import config
# print (config.TestPlanUrl)


class MyTest(unittest.TestCase):
    def setUp(self):
        print('start test')
        pass
    def tearDown(self):
        print('end test')
        pass
class test_queryEduReport(MyTest):
    '''测试接口：1.	电信诈骗学历统计'''

    def test_queryEduReport(self):
        '''测试用例1：1.	电信诈骗学历统计'''

        #        ==================post请求==================================
        # 登录验证获取cookies
        self.url = (config.TestPlanUrl) + "/affairs/analysis/home/check.do?"
        self.data = {
            "colUsername": "admin",
            "colPassword": 11111111

        }
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(url=self.url, json=self.data, headers=self.headers)

        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("0", self.r.text)


        cookies = self.r.cookies

        #        ==================post请求==================================

        self.url = (config.TestPlanUrl) + "/affairs/swindle/swindle/queryEduReport.do?"
        self.data = {

            "ajxl": "电信诈骗:01",
            "gxpcsbm": "120103410000",


        }
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(url=self.url, json=self.data, headers=self.headers,cookies=cookies)

        #=============================================================
        print(self.r)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()