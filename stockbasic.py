#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stockbasic.py
@Time    :   2021/03/06 22:39:26
@Author  :   Ocean 
@Version :   1.0
@Contact :   dazekey@163.com
@License :   (C)Copyright 2017-2018, Ocean&HappyFriends
@Desc    :   None
@Subject :   无关于tradedate, code的数据
'''

# here put the import lib
import utils as uts

class StockBasic(object):

    def __init__(self, start, end):
        self.start = start 
        self.end = end

    @property
    def stock_basic(self):
        df = uts.get_stock_basic(self)
        return df

    
    def get_calendar_df(self):
        """
        return: df
        """
        self.calendar_df = uts.get_calendar_df(self.start, self.end)
        return self.calendar_df

    @property
    def calendar_day(self):
        """
        return: list
        """
        if self.calendar_df == None:
            self.get_calendar_df()

        res = self.calendar_df.copy()
        return res["cal_date"].tolist()

    @property
    def trade_calendar(self):
        """
        return: list
        """
        if self.calendar_df == None:
            self.get_calendar_df()
        res = self.calendar_df.copy()
        res = res.loc[res["is_open"]==1]
        return res["cal_date"].tolist()

    
if __name__ == "__main__":
    stockbasic = StockBasic("20210101", "20210201")
    print(stockbasic.trade_calendar)
