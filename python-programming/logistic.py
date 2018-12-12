import pandas as pd
from sklearn.metrics import confusion_matrix
import sklearn.linear_model as lm
clf = lm.LogisticRegression(C=10.0)

grades = pd.read_table("grades.csv")
labels = ('F','D','C','B','A')
grades["Letter"] = pd.cut(grades["Final score"], [0,60,70,80,90,100],
                        labels = labels)
X = grades[["Quiz 1","Quiz 2"]]
clf.fit(X, grades["Letter"])
print("Score = %.3f"%clf.score(X, grades["Letter"]))
cm = confusion_matrix(clf.predict(X),grades["Letter"])
print(pd.DataFrame(cm,columns = labels, index = labels))