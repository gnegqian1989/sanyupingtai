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
class test_queryOldData(MyTest):
    '''测试接口：1.	1.	2.	选择历史时间，列表数据'''

    def test_queryOldData(self):
        '''测试用例1：1.	1.	2.	选择历史时间，列表数据'''

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

        #        ==================get请求==================================

        self.url =(config.TestPlanUrl) +"/affairs/analysis/forcast/queryOldData.do?"\
                                        "dtDate=2018-11-23&" \
                                        "strCode=01030301&" \
                                        "timeDate=night&" \
                                        "strBranchCodes=120104000000&"


        print(self.url)
        self.headers = {"Content-Type":"application/json"}

        self.r = requests.get(url = self.url,cookies=cookies)
        # return self.r.json()


        #=============================================================
        print(self.r)
        print(self.r.text)
        print(self.r.status_code)
        self.assertIn("200",self.r.text)

if __name__ =="__main__":
        unittest.main()