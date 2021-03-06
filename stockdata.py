#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockdata.py
@Time    :   2021/03/06 20:16:00
@Author  :   Ocean 
@Version :   1.0
@Contact :   dazekey@163.com
@License :   (C)Copyright 2017-2018, Ocean&HappyFriends
@Desc    :   None
@Subject :   None
'''

# here put the import lib
import utils as uts

class StockData(object):

    def __init__(self, code, start, end , adj="hfq"):
        self.code = code 
        self.start = start
        self.end = end
        self.adj = adj

        self.calendar_df = None

    @property
    def price_daily(self):
        """
        return: df
        """
        res = uts.get_price_daily(self.code, self.start, self.end)
        return res

    @property
    def adjust_price_daily(self, adj=None):
        adj = adj or self.adj
        res = uts.get_adjust_price_daily(self.code, adj, self.start,\
                                    self.end)
        return res
    
    @property 
    def daily_indicator(self):
        df = uts.get_daily_indicator_by_code(self.code, \
                        self.start, self.end)
        
        return df

if __name__ == "__main__":
    payh = StockData("000001.SZ", "20180101", "20210101")
    # print(payh.calendar_day)
    # print(payh.trade_calendar)
    # print(payh.price_daily)
    # print(payh.adjust_price_daily)
    print(payh.daily_indicator)