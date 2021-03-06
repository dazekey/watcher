#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   util_tushare.py
@Time    :   2021/03/06 20:59:26
@Author  :   Ocean 
@Version :   1.0
@Contact :   dazekey@163.com
@License :   (C)Copyright 2017-2018, Ocean&HappyFriends
@Desc    :   None
@Subject :   None
'''

# here put the import lib
import tushare as ts
from config import TSTOKEN

pro = ts.pro_api(TSTOKEN)

def get_calendar_df(start, end):
    res = pro.query('trade_cal', start_date=start, \
                        end_date=end) 
    return res

def get_price_daily(code, start, end):
    res = pro.query('daily', ts_code=code, \
                    start_date=start, end_date=end)
    return res

def get_adjust_price_daily(code, adj, start, end):
    res = ts.pro_bar(ts_code=code, \
                            adj=adj, start_date=start, \
                            end_date=end) 
    return res

def get_daily_indicator_by_code(code, start, end, fields=""):
    df = pro.query('daily_basic', ts_code=code, \
                start_date=start, end_date = end,
                fields=fields)
    return df

def get_daily_indicator_by_tradedate(trade_date, fields):
    df = pro.query('daily_basic', ts_code='', \
                    trade_date=trade_date,
                    fields=fields)
    return df

def get_stock_basic(code, exchange="", list_status="L", fields=""):
    df  = pro.query('stock_basic', exchange=exchange, \
                    list_status=list_status, fields=fields)
    return df
