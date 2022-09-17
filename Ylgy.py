#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json

class Ylgy:
    apiUrl = "https://cat-match.easygame2021.com"

    def __init__(self, Token, Uid):
        self.Token = Token
        self.Uid = Uid

    #用现有token获取目标uid的openid
    def getOpenId(self):
        try:
            ret = json.loads(requests.get(self.apiUrl + "/sheep/v1/game/user_info?uid=" + self.Uid,headers={'t':self.Token},timeout=10).text)
        except:
            print("获取用户信息 => 请求失败！")
            return False
        print(ret)
        if ret['err_code'] != 0:
            print("用户信息获取失败 =>", ret['err_code'])
            return False
        else:
            print("用户信息获取成功", "Nick:", ret['data']['nick_name'], "WxOpenId:", ret['data']['wx_open_id'])
            self.openId = ret['data']['wx_open_id']
            return True
    #用获取到的openid转换成token
    def openIdLogin(self):
        try:
            ret = json.loads(requests.post(self.apiUrl + "/sheep/v1/user/login_tourist", data={'uuid':self.openId}, headers={'t': self.Token},timeout=10).text)
        except:
            print("openId登录 => 请求失败！")
            return False
        print(ret)
        if ret['err_code'] != 0:
            print("openId登录失败 =>", ret['err_code'])
            return False
        else:
            print("openId登录成功", "Uid:", ret['data']['uid'], "Token:", ret['data']['token'])

            if str(ret['data']['uid']) != self.Uid:
                print("Uid不匹配")
                return False
            else:
                self.userToken = ret['data']['token']
                return True

    def run(self,overTime):
        if self.userToken == '':
            print('Token获取失败')
            return False
        #通关时长
        if overTime == 0:
            overTime = 60

        try:
            ret = json.loads(requests.get(self.apiUrl + "/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time="+str(overTime)+"&rank_role=1&skin=1", headers={'t': self.userToken},timeout=10).text)
        except:
            print("提交通关信息 => 请求失败！")
            return False
        print(ret)
        if ret['err_code'] != 0:
            print("提交通关信息失败 =>", ret['err_code'])
            return False
        else:
            print("提交成功！")
            return True
