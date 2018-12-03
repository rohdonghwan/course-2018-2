import numpy
import pandas as pd
print("<<Pandas 데이터 구조에 익숙해지기>>")
inflation = pd.Series((2.2,3.4,2.8,1.6,2.3,2.7,3.4,3.2,2.8,3.8,-0.4,1.6,3.2,2.1,1.5,1.5))
print(inflation)
print(inflation.values)
print(inflation.index.values)
inflation.index = pd.Index(range(1999,2015))
inflation[2015] = numpy.nan
inflation.index.name = "Year"
inflation.name = "%"
print(inflation.head())
print(inflation.tail())
alco2009 = pd.read_csv("niaaa-report2009.csv", index_col = "State")
print(alco2009)
alco2009["Wine"].head()
alco2009["Total"] = 0
print(alco2009.head())
print("")

print("<<데이터 모양 바꾸기>>")
print(alco2009.columns.values)
alco2009.reset_index().set_index("Beer").head()
"Samoa" in alco2009.index
s_states = [state for state in alco2009.index if state[0] == 's']+["Samoa"]
print(s_states)
drinks = list(alco2009.columns)+["Water"]
print(drinks)
nan_alco = alco2009.reindex(s_states, columns = drinks)
print(nan_alco) 
alco = pd.read_csv("niaaa-report.csv",index_col=["state","Year"])
print(alco)
nan_alco.dropna(how="all")
nan_alco.dropna(how="all", axis = 1)

print(nan_alco.isnull())
print(nan_alco_notnull())
sp = nan_alco["Sprits"]
clean = sp.notnull()
sp[-clean] = sp[clean].mean()
print(nan_alco)
print(nan_alco.fillna(0))
print(nan_alco.fillna(method = "ffill"))
