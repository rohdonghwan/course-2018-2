import statistics as stcs
from scipy.stats import pearsonr as pr
import pandas as pd
stock=pd.read_csv("^GSPC.csv", index_col = "Date")
print(stock["Close"].mean())
print(stock["Close"].std())
print(stock["Close"].skew())
print(pr(stock["Close"],stock["Volume"]))