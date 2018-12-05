import pandas as pd
lynx = pd.read_csv("lynx.csv", index_col = ["Year"])
print(lynx)
lynx.dropna(axis = 1)