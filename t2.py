import tushare as ts
from config import tushare_token

print("tushare_token", tushare_token)
ts.set_token(tushare_token)
pro = ts.pro_api()
df = pro.daily(trade_date="20250730")


print(df)
