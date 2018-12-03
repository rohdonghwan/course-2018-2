import numpy as np

stock = np.array([140.49, 0.97,40.68,41.53,55.7,57.21,98.2,99.19,109.96,111.47,35.71,36.27,87.85,89.11,30.22,30.91])
print(stock)
stocks = stock.reshape(8,2).T
print(stocks)

sap = np.array(["MMM", "ABT", "ABBV","ACN","ACE","ATVI","ADBE","ADT"])
print(sap)

fall = np.greater(stocks[0], stocks[1])
print(fall)
sap[fall]

stocks[1,0] = np
np.isnan(stocks)

stocks[np.isnan(stocks)] = 0
print(stocks)

RATE = .375
TERM = 30
simple = (  RATE*np.ones(TERM)).cumsum()
compound = ((1+RATE)*np.ones(TERM)).cumprod()
print(simple)
print(compound)
diffSimple = np.abs(simple[0] - simple[-1])
print(diffSimple)