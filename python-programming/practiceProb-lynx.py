import pandas as pd
lynx = pd.read_csv("lynx.csv")
print(lynx)
lynx["Year"] = lynx.Year/10
lynx["Year"] = lynx["Year"].round()*10
print(lynx)
sum_lynx = lynx.groupby("Year").sum()
result = sum_lynx.sort_values("hunted",ascending = False)
print(result)