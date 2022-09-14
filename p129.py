import csv

dataset1 = []
dataset2 = []

with open("star_data.csv","r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset1.append(row)

with open("dwarf_stars.csv","r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        dataset2.append(row)

header1 = dataset1[0]
planet_data1 = dataset1[1:]

header2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = header1 + header2
planet_data = []

for index,datarow in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("merged_data.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)