#converteste fisierul din csv in json 
#converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
#converteste un fisier json primit ca parametru in fisier csv (pe caz general)

import json
import csv



def csvTojson(inputCsv, outputJson):
    infile = open(inputCsv, "r", encoding = "utf-8-sig")
    content = csv.DictReader(infile, dialect = "excel")

    resultList = []
    for row in content:
        resultList.append(row)

    infile.close()

    outfile = open(outputJson, "w")
    outfile.write(json.dumps(resultList))
    outfile.close()



def txtOut(inputCsv, outputTxt):
    infile = open(inputCsv, "r", encoding="utf-8-sig")
    content = csv.DictReader(infile, dialect="excel")
    checkedVehicles = []

    pastRow = {}
    for row in content:
        if len(checkedVehicles) == 0:
            pastRow = row
            checkedVehicles.append(row)
        else:
            if row["JUDET"] == pastRow["JUDET"]:
                if row["MARCA"] == pastRow["MARCA"]:
                    checkedVehicles[len(checkedVehicles)-1]["TOTAL_VEHICULE"] = int(checkedVehicles[len(checkedVehicles)-1]["TOTAL_VEHICULE"]) + int(row["TOTAL_VEHICULE"])
                else:
                    checkedVehicles.append(row)
            else:
                checkedVehicles.append(row)
        pastRow = row
    
    infile.close()

    outfile = open(outputTxt, "w")
    for line in checkedVehicles:
        outfile.write(f"Vehicul de tip {line['CATEGORIE_NATIONALA']} din judetul {line['JUDET']} marca {line['MARCA']}: {line['TOTAL_VEHICULE']}\n")
    outfile.close()



def jsonToCsv(inputJson, outputCsv):
    with open(inputJson, "r") as jsonFile:
        jsonObj = json.load(jsonFile)
    
    headers = list(jsonObj[0].keys())
    with open(outputCsv, "w") as csvFile:
        linewriter = csv.DictWriter(csvFile, fieldnames=headers)
        linewriter.writeheader()
        for line in jsonObj:
            linewriter.writerow(line)

