import pandas as pd

population = pd.read_csv("population.csv", index_col = "State")
alco2009 = pd.read_csv("niaaa-report2009.csv", index_col = "State")
alco = pd.read_csv("niaaa-report.csv", index_col = "State")

print(population.head)
print("")

print(alco2009)
print("")

print("<max>")
print(alco2009.max(axis = 1))
print("")

print("<min>")
print(alco2009.min(axis = 0))
print("")

print("<Total>")
alco["Total"] = alco.Wine + alco.Spirits + alco.Beer
print(alco.head())
print("")

print("<DNA>")
dna = "AGCTTATAACGGCGAGAATTCCCGCTACACCACATCATGCGGC"
dna_as_series = pd.Series(list(dna),name = "genes")
print(dna_as_series.head())
print(dna_as_series.unique())
dna_as_series.value_counts().sort_index()
valid_nucs = list("ACGT")
dna_as_series.isin(valid_nucs).all()
dna1 = dna.replace("C","")
dna2 = dna.replace("T","")
dna_as_series1 = pd.Series(list(dna1), name = "genes")
dna_as_series2 = pd.Series(list(dna2), name = "genes")
print(dna_as_series1.value_counts()+dna_as_series2.value_counts())
print("")

print("<Aggregation>")
alco_noidx = alco.reset_index()
sum_alco = alco_noidx.groupby("Year").sum()
print(sum_alco.tail())
print("")

print("<Discrete>")
wine_state = alco2009["Wine"] > alco2009["Wine"].mean()
beer_state = alco2009["Beer"] > alco2009["Beer"].mean()
pd.crosstab(wine_state, beer_state)
print("")