import pandas as pd

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col = "State")
df = pd.merge(alco2009.reset_index(),population.reset_index()).set_index("state")
print(df.head())

population = pd.read_csv("population.csv", index_col = "State")
population.head()
