import matplotlib, matplotlib.pyplot as plt
import pickle, pandas as pd
import sklearn.cluster, sklearn.preprocessing
alco2009 = pickle.load(open("alco2009.pickle","rb"))
states = pd.read_csv("states2.csv", names = ("State", "Standard", "Postal","Capital"), skiprows = 1)
columns = ["Wine","Beer"]
kmeans = sklearn.cluster.KMeans(n_clusters = 9)
kmeans.fit(alco2009[columns])
alco2009["Clusters"] = kmeans.labels_
centers = pd.DataFrame(kmeans.cluster_centers_, columns = columns)
matplotlib.style.use("ggplot")
ax = alco2009.plot.scatter(columns[0],columns[1], c = "Clusters", cmap = plt.cm.Accent , s = 100)
centers.plot.scatter(columns[0], columns[1],color = "red",marker = "*",
                    s =200, ax = ax)

def add_addr(state):
    _ = ax.annotate(state["Postal"],state[columns],xytext = (1,5),
                    textcoords = "offset points",size = 8,
                    color = "darkslategrey")

alco2009withStates = pd.concat([alco2009, states.set_index("State")],
                                axis = 1,sort = True)
alco2009withStates.apply(add_addr, axis = 1)

plt.title("US States Clustered by Alcohol Consumption")
plt.savefig("clusters.pdf")