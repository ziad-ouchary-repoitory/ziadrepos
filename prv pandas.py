import pandas as pd

from pandas_datareader import data

df = data.get_data_yahoo("AAPL")

print(df.sum())
print()
print(df.sum() / df.count() == df.mean())