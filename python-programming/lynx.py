import pandas as pd
lynx = pd.read_csv("lynx.csv")
lynx["time"] = round(lynx["time"]/10)
lynx["time"] = lynx["time"]*10
lynx_sum = lynx.groupby("time").sum()
print(lynx_sum.sort_values("value",ascending = False))