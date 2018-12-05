import pandas as pd

population = pd.read_csv("population.csv", index_col = "State")
alco2009 = pd.read_csv("niaaa-report2009.csv", index_col = "State")

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

print("<DNA>")
dna = "AGCTTATAACGGCGAGAATTCCCGCTACACCACATCATGCGGC"
dna_as_series = pd.Series(list(dna),name = "genes")
print(dna_as_series.head())
print(dna_as_series.unique())
dna_as_series.value_counts().sort_index()
valid_nucs = list("ACGT")
dna_as_series.isin(valid_nucs).all()
print("")