# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:33:52 2020

@author: Charlot
"""

# date:一个理想化的简单型日期， Ymd
# time: 一个独立于任何特定日期的理想化时间，它假设每一天都恰好等于 24*60*60 秒
# datetime:日期和时间的结合， Y-m-d H:M:S.fff
# timedelta:表示两个 date 对象或者 time 对象,或者 datetime 对象之间的时间间隔，精确到微秒
# tzinfo: 时区信息
# timezone: UTC时区


from datetime import date

print(date.today())

from datetime import datetime

# 2者一样
print(datetime.today())
print(datetime.now())

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
print(datetime.now().weekday()) # 返回一个整数代表星期几，星期一为 0，星期天为 6。
print(datetime.now().isoweekday()) # 返回一个整数代表星期几，星期一为 1，星期天为 7


from datetime import timedelta
print(datetime.now()+timedelta(days=10))

