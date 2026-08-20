"""获取牧原股份8/20实时盘中数据"""
import os
import tushare as ts
import pandas as pd
import time

os.environ['TUSHARE_TOKEN'] = '9f640d421f866dde9a1888ab4193f77c43659d47446d717ffa343023'
ts.set_token(os.environ['TUSHARE_TOKEN'])
pro = ts.pro_api()

ts_code = '002714.SZ'

# 1. 确认8/20是否为交易日
tc = pro.trade_cal(exchange='SSE', start_date='20260820', end_date='20260820')
print("=== 8/20 trade_cal ===")
print(tc.to_string(index=False))

# 2. 尝试实时分钟数据 rt_min
print("\n=== 尝试 rt_min (实时分钟) ===")
try:
    rt = pro.rt_min(ts_code=ts_code)
    print(f"rt_min rows: {len(rt)}")
    if len(rt) > 0:
        print(rt.tail(5).to_string(index=False))
        print(f"\n最新价: {rt.iloc[-1]['price']}")
except Exception as e:
    print(f"rt_min error: {e}")

# 3. 尝试 stk_mins (1分钟K线)
print("\n=== 尝试 stk_mins (1分钟K线) ===")
try:
    today = '20260820'
    mins = pro.stk_mins(ts_code=ts_code, start_date=today + ' 09:00:00', end_date=today + ' 15:00:00', freq='1min')
    print(f"stk_mins rows: {len(mins)}")
    if len(mins) > 0:
        print(mins.tail(10).to_string(index=False))
except Exception as e:
    print(f"stk_mins error: {e}")

# 4. 尝试 daily_basic 获取今日收盘数据（如果已更新）
print("\n=== daily_basic 8/20 ===")
try:
    db = pro.daily_basic(ts_code=ts_code, start_date='20260820', end_date='20260820')
    print(f"daily_basic rows: {len(db)}")
    if len(db) > 0:
        print(db.to_string(index=False))
except Exception as e:
    print(f"daily_basic error: {e}")

# 5. 尝试 daily 获取8/20数据
print("\n=== daily 8/20 ===")
try:
    daily = pro.daily(ts_code=ts_code, start_date='20260820', end_date='20260820')
    print(f"daily rows: {len(daily)}")
    if len(daily) > 0:
        print(daily.to_string(index=False))
except Exception as e:
    print(f"daily error: {e}")

# 6. 尝试 moneyflow 8/20
print("\n=== moneyflow 8/20 ===")
try:
    mf = pro.moneyflow(ts_code=ts_code, start_date='20260820', end_date='20260820')
    print(f"moneyflow rows: {len(mf)}")
    if len(mf) > 0:
        print(mf.to_string(index=False))
except Exception as e:
    print(f"moneyflow error: {e}")
