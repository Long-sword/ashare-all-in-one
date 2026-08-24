"""获取卫星化学8/20实时+历史数据"""
import os
import urllib.request
import tushare as ts
import pandas as pd

os.environ['TUSHARE_TOKEN'] = '9f640d421f866dde9a1888ab4193f77c43659d47446d717ffa343023'
ts.set_token(os.environ['TUSHARE_TOKEN'])
pro = ts.pro_api()
ts_code = '002648.SZ'

# 1. 新浪实时
print("=== 新浪实时行情 ===")
try:
    url = 'http://hq.sinajs.cn/list=sz002648'
    req = urllib.request.Request(url, headers={
        'Referer': 'http://finance.sina.com.cn',
        'User-Agent': 'Mozilla/5.0'
    })
    resp = urllib.request.urlopen(req, timeout=10)
    data = resp.read().decode('gbk')
    fields = data.split(',')
    if len(fields) > 3:
        print(f"名称: {fields[0].split('=\"')[1]}")
        print(f"今开: {fields[1]}")
        print(f"昨收: {fields[2]}")
        print(f"最新价: {fields[3]}")
        print(f"最高: {fields[4]}")
        print(f"最低: {fields[5]}")
        print(f"成交量(手): {fields[8]}")
        print(f"成交额: {fields[9]}")
        print(f"日期: {fields[30]}")
        print(f"时间: {fields[31]}")
except Exception as e:
    print(f"新浪 error: {e}")

# 2. 腾讯实时
print("\n=== 腾讯实时行情 ===")
try:
    url = 'http://qt.gtimg.cn/q=sz002648'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req, timeout=10)
    data = resp.read().decode('gbk')
    fields = data.split('~')
    if len(fields) > 10:
        print(f"名称: {fields[1]}")
        print(f"最新价: {fields[3]}")
        print(f"昨收: {fields[4]}")
        print(f"今开: {fields[5]}")
        print(f"成交量(手): {fields[6]}")
        print(f"最高: {fields[33]}")
        print(f"最低: {fields[34]}")
        print(f"成交额(万): {fields[37]}")
        print(f"换手率: {fields[38]}")
        print(f"市盈率: {fields[39]}")
        print(f"量比: {fields[49]}")
        print(f"市净率: {fields[46] if len(fields)>46 else 'N/A'}")
except Exception as e:
    print(f"腾讯 error: {e}")

# 3. Tushare日线 8月
print("\n=== Tushare daily 8月 ===")
daily = pro.daily(ts_code=ts_code, start_date='20260720', end_date='20260820')
daily = daily.sort_values('trade_date').reset_index(drop=True)
print(daily.to_string(index=False))

# 4. 资金流
print("\n=== Tushare moneyflow 8月 ===")
mf = pro.moneyflow(ts_code=ts_code, start_date='20260801', end_date='20260820')
mf = mf.sort_values('trade_date').reset_index(drop=True)
print(mf.to_string(index=False))

# 5. 基本面
print("\n=== Tushare daily_basic 8月 ===")
db = pro.daily_basic(ts_code=ts_code, start_date='20260801', end_date='20260820')
db = db.sort_values('trade_date').reset_index(drop=True)
print(db.to_string(index=False))

# 6. 财务指标
print("\n=== Tushare fina_indicator 2025年报 ===")
try:
    fi = pro.fina_indicator(ts_code=ts_code, period='20251231')
    if len(fi) > 0:
        cols = ['ts_code','end_date','eps','bps','roe','grossprofit_margin','netprofit_margin',
                'tr_yoy','netprofit_yoy','dt_netprofit_yoy','op_yoy','debt_to_assets',
                'current_ratio','quick_ratio','q_roe','roe_yoy']
        avail_cols = [c for c in cols if c in fi.columns]
        print(fi[avail_cols].to_string(index=False))
except Exception as e:
    print(f"fina_indicator error: {e}")

# 7. 股票基本信息
print("\n=== stock_basic ===")
basic = pro.stock_basic(ts_code=ts_code)
print(basic[['ts_code','symbol','name','area','industry','market','list_date']].to_string(index=False))
