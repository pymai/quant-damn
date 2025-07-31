import pandas as pd

path = "stock_daily/20250731.pkl"

df = pd.read_pickle(path)

print(df)
