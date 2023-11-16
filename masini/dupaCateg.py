import pandas as pd

df = pd.read_csv("/Users/bindarclaudiu-andrei/Documents/K/Curs/curs17/masini/masini.csv")

def MasiniCategorie(param):
    categorie = df[(df['CATEGORIE_NATIONALA'] == param)]
    for row in categorie['MARCA'].values:
        print(row)

# MasiniCategorie("AUTOBUZ")
