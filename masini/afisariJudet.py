import pandas as pd

df = pd.read_csv("/Users/bindarclaudiu-andrei/Documents/K/Curs/curs17/masini/masini.csv")

def AfisareJud(Judet):
    zone = df[(df['JUDET'] == Judet)]
    for row in zone['MARCA'].values:
        print(row)

AfisareJud('VRANCEA')

# def MasiniDinCategorie(Categorie):





    
        

