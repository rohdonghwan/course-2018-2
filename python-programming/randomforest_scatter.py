from sklearn.ensemble import RandomForestRegressor
import pandas as pd, numpy.random as rnd
import matplotlib, matplotlib.pyplot as plt

hed = pd.read_csv('Hedonic.csv')
selection = rnd.binomial(1,0.7, size = len(hed)).astype(bool)
training = hed[selection]
testing = hed[~selection]

rfr = RandomForestRegressor()
predictors_tra = training.ix[:,"crim":"lstat"]
predictors_tst = testing.ix[:,"crim":"lstat"]

feature = "medv"
rfr.fit(predictors_tra, training[feature])

matplotlib.style.use("ggplot")

plt.scatter(training[feature],rfr.predict(predictors_tra), c = "green", s = 50)
plt.scatter(testing[feature],rfr.predict(predictors_tst), c = "red")
plt.legend(["Training data", "Testing data"], loc = "upper left")
plt.plot(training[feature],training[feature], c = "blue")
plt.title("Hedonic prices of Census Tracts in the Boston Area")
plt.xlabel("Actual value")
plt.ylabel("Predicted value")
plt.savefig("rfr.pdf")