import pandas as pd

df = pd.read_csv("/Users/bindarclaudiu-andrei/Documents/K/Curs/curs17/masini/masini.csv")

def pesteZeceMasini():
    nrMasini = df[(df['TOTAL_VEHICULE'] >= 10)]
    for row in nrMasini['MARCA'].values:
        print(row)

pesteZeceMasini()