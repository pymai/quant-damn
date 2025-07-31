import tushare as ts
from config import tushare_token
import datetime
import os

print("tushare_token", tushare_token)
ts.set_token(tushare_token)
pro = ts.pro_api()
# 设定获取日线行情的初始日期和终止日期，其中终止日期设定为昨天。
# start_dt = "20200101"
time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
end_dt = time_temp.strftime("%Y%m%d")

# 创建stock_daily目录（如果不存在）
os.makedirs("stock_daily", exist_ok=True)

with open("all_workday.txt", "r") as f:
    for line in f:
        day = line.strip("\n")
        # 转换日期格式为 YYYYMMDD (tushare需要的格式)
        trade_date = day.replace("-", "")
        # 只处理2025年及以后的日期，并且不超过 end_dt
        if day >= "2025-01-01" and trade_date <= end_dt:
            file_path = f"stock_daily/{trade_date}.pkl"
            # 如果文件已存在，跳过获取
            if os.path.exists(file_path):
                print(f"文件已存在，跳过: {day} ({trade_date})")
                continue

            print(f"获取日期: {day} ({trade_date})")
            df = pro.daily(trade_date=trade_date)
            print(df)
            df.to_pickle(file_path)
