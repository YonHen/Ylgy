#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Ylgy import Ylgy
def main():
    #随便填写一个Token
    Token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQyODEzMjgsIm5iZiI6MTY2MzE3OTEyOCwiaWF0IjoxNjYzMTc3MzI4LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo1NTgzNDY1OCwiZGVidWciOiIiLCJsYW5nIjoiIn0.7r3lECqC87vGBrp8gX2TWO6iwKm5WjS_A2gq1BXC4Hc"
    #目标UId
    Uid = "1000001"
    #次数
    times = 100
    #通关时长 (秒)
    overTime = 60

    obj = Ylgy(Token,Uid)

    #获取Token过程
    if obj.getOpenId():
        if obj.openIdLogin():
            print("获取token成功！")
        else:
            print("获取token失败！")
            return 0
    else:
        print("获取openId失败！")
        return 0
    #开刷！
    for i in range(times):
        obj.run(overTime)

if __name__ == "__main__":
    main()
