#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sectiondata.py
@Time    :   2021/03/06 20:58:53
@Author  :   Ocean 
@Version :   1.0
@Contact :   dazekey@163.com
@License :   (C)Copyright 2017-2018, Ocean&HappyFriends
@Desc    :   None
@Subject :   截面数据，按日期获取截面
'''

# here put the import lib
import utils as uts

class SectionData(object):

    def __init__(self, trade_date):
        self.trade_date = trade_date
    


if __name__ == "__main__":
    secdata = SectionData("20210201")
    print(secdata.stock_basic)