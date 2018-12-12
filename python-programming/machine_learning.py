import numpy, pandas as pd
import matplotlib, matplotlib.pyplot as plt
import sklearn.linear_model as lm
sap = pd.read_csv("sapXXI.csv").set_index("Date")

sap.index = pd.to_datetime(sap.index)
sap_linear = sap.ix[sap.index > pd.to_datetime('2009-01-01')]
olm = lm.LinearRegression()
x = numpy.array([x.toordinal() for x in sap_linear.index])[:,
    numpy.newaxis]
y = sap_linear['Close']
olm.fit(x,y)
yp = [olm.predict(x.toordinal())[0]for x in sap_linear.index]

olm_score = olm.score(x,y)

matplotlib.style.use("ggplot")
plt.plot(sap_linear.index,y)
plt.plot(sap_linear.index, yp)
plt.title("OLS Regression")
plt.xlabel("Year")
plt.ylabel("S&P 500(closing)")
plt.legend(["Actual", "Predicted"], loc = "lower right")
plt.annotate("Score = %.3f"%olm_score,
            xy=(pd.to_datetime('2010-06-01').toordinal(),1900))

plt.savefig("sap-linregr.pdf")