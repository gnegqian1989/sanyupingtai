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
class test_queryDetails(MyTest):
    '''测试接口：1.	1.	2.	3.	地图显示打点'''

    def test_queryDetails(self):
        '''测试用例1：1.	1.	2.	3.	地图显示打点'''

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

        self.url =(config.TestPlanUrl) +"/affairs/analysis/forcast/queryDetails.do?"\
                                        "fk_bas_police_custom_class_id=01030301&" \
                                        "forecast_date=0000-00-00&"




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